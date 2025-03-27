import torch
import torch.nn as nn
from torch.utils.checkpoint import checkpoint
from gpu_aware_mpi import get_size, get_rank, allgather, reduce_scatter

import gc
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FSDPLayer(nn.Module):
    def __init__(self, module, should_checkpoint=False):
        super().__init__()
        self.module = module
        self.shard_parameters()

        self.module.register_full_backward_hook(self._full_backward_hook)

        self.should_checkpoint = should_checkpoint

    def _full_backward_hook(self, module, grad_input, grad_output):
        self.free_params()

    def shard_parameters(self):
        self.sharded_parameter_metadata = {}

        logger.debug(f"Rank {rank}: Sharding parameters for {self.module}")

        for name, param in list(self.module.named_parameters(recurse=False)):
            shard, metadata_dict = shard_tensor(param)

            self.sharded_parameter_metadata[name] = metadata_dict

            logger.debug(
                f" Rank {rank}: Sharding parameter {name} with shape {param.shape} into {metadata_dict}, new shape {shard.shape}"
            )

            setattr(
                self.module,
                "shard_" + name,
                nn.Parameter(shard, requires_grad=param.requires_grad),
            )
            delattr(self.module, name)
            setattr(self.module, name, shard)

        logger.debug(
            f" Rank {rank}: Sharded parameters are {[i[0] for i in self.module.named_parameters(recurse=False)]}"
        )

    def forward(self, *args, **kwargs):
        if self.should_checkpoint:
            return checkpoint(self.forward_op, *args, use_reentrant=True, **kwargs)
        else:
            return self.forward_op(*args, **kwargs)

    def forward_op(self, *args, **kwargs):
        self.gather_all_parameters()
        result = self.module(*args, **kwargs)

        self.free_params()

        return result

    def gather_all_parameters(self):
        logger.debug(f"Rank {rank}: Gathering parameters for {self.module}")

        for name, param in self.module.named_parameters(recurse=False):

            if not name.startswith("shard_"):
                logger.debug(f" Rank {rank}: Skipping parameter {name}")
                continue

            # Remove _shard_ prefix
            name = name[6:]

            # Get metadata for this parameter
            metadata_dict = self.sharded_parameter_metadata[name]

            # Gather all shards and reconstruct the full tensor
            full_tensor = all_gather_op(param, metadata_dict)

            logger.debug(
               f" Rank {rank}: Gathered parameter {name} with shape {full_tensor.shape}"
            )

            # Copy the full tensor back to the original parameter
            setattr(self.module, name, full_tensor)

    def free_params(self):
        for name, param in self.module.named_parameters(recurse=False):

            if not name.startswith("shard_"):
                #logger.debug(f" Rank {rank}: Skipping parameter {name}")
                continue

            # Remove _shard_ prefix
            name = name[6:]

            if hasattr(self.module, name):
                if getattr(self.module, name).data_ptr() != param.data.data_ptr():
                    delattr(self.module, name)

            setattr(self.module, name, param.data)

        gc.collect()
        torch.cuda.empty_cache()

    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError:
            return getattr(self.module, name)

    def free_params(self):
        for name, param in self.module.named_parameters(recurse=False):

            if not name.startswith("shard_"):
                #logger.debug(f" Rank {rank}: Skipping parameter {name}")
                continue

            # Remove _shard_ prefix
            name = name[6:]

            if hasattr(self.module, name):
                if getattr(self.module, name).data_ptr() != param.data.data_ptr():
                    delattr(self.module, name)

            setattr(self.module, name, param.data)

        gc.collect()
        torch.cuda.empty_cache()


class SimpleFSDP(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self._wrap_layers(model)

    def _wrap_layers(self, module):
        for name, child in module.named_children():
            params = list(child.parameters(recurse=False))

            grand_children = list(child.children())

            has_grand_children = False
            if len(grand_children) > 0:
                has_grand_children = True

            if len(params) > 0:
                wrapped = FSDPLayer(child, should_checkpoint=has_grand_children)
                setattr(module, name, wrapped)

            if has_grand_children:
                self._wrap_layers(child)

    def forward(self, *args, **kwargs):
        return self.model(*args, **kwargs)

    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError:
            return getattr(self.model, name)


world_size = get_size()
rank = get_rank()

def shard_tensor(tensor):
    """Evenly shard tensor across ranks with padding if needed.
    Returns (shard, metadata_dict) where metadata_dict contains
    {rank: (original_numel, original_shape)} for all ranks."""
    original_shape = tensor.shape
    original_numel = tensor.numel()

    # Calculate padding for equal division
    padded_numel = ((original_numel + world_size - 1) // world_size) * world_size
    padding = padded_numel - original_numel

    # Pad tensor if needed
    if padding > 0:
        tensor_padded = torch.cat(
            [tensor.view(-1), torch.zeros(padding, device=tensor.device)]
        )
    else:
        tensor_padded = tensor.view(-1)

    # Split into equal shards
    shard_size = padded_numel // world_size
    start = rank * shard_size
    shard = tensor_padded[start : start + shard_size].clone()

    # Gather metadata from all ranks
    local_metadata = torch.tensor([original_numel, *original_shape, shard_size, padding], dtype=torch.long)
    all_metadata = torch.zeros((world_size, local_metadata.numel()), dtype=torch.long)
    allgather(local_metadata, all_metadata)

    # Create a dictionary of metadata keyed by rank
    metadata_dict = {rank: all_metadata[rank].tolist() for rank in range(world_size)}

    # Convert metadata back to original format
    metadata_dict = {rank: (meta[0], tuple(meta[1:-2]), meta[-2], meta[-1]) for rank, meta in metadata_dict.items()}
    
    return shard, metadata_dict


def trim_padding(all_tensors, rank, world_size, metadata_dict):

    original_numel, _, shard_size, padding = metadata_dict[rank]

    if padding == 0:
        return all_tensors

    # all_tensors is a list of tensors that have been collected
    if padding > shard_size:
        # Calculate the number of fully padded tensors
        fully_padded_tensors = padding // shard_size

        # Remove fully padded tensors
        all_tensors = all_tensors[:-fully_padded_tensors]

        # Calculate the remaining padding in the last tensor
        remaining_padding = padding % shard_size

        # Trim the remaining padding from the last tensor
        if remaining_padding > 0 and len(all_tensors) > 0:
            last_tensor = all_tensors[-1]
            all_tensors[-1] = last_tensor[:-remaining_padding]
    else:
        # trim padding for last rank
        if rank == world_size - 1:
            valid_elements = original_numel - (world_size - 1) * shard_size
            all_tensors[-1] = all_tensors[-1][:valid_elements]


    return all_tensors

def collectives_all_gather(shard, metadata_dict):
    """Gather shards and reconstruct the full tensor using metadata."""
    # Prepare buffers
    gathered = torch.empty(shard.numel() * world_size, device=shard.device, dtype=shard.dtype).contiguous().detach()
    shard_detached = shard.contiguous().detach()

    # Collective operation
    start = time.time()
    allgather(shard_detached, gathered)
    end = time.time()
    
    total_time = "{:.1e}".format(end - start)
    bandwidth = "{:.1e}".format(shard_detached.nbytes / (end - start) / 1e9)
    logger.info(f"All_gather time on device {shard_detached.device}: {total_time}, bandwidth: {bandwidth} GB/s on tensor {shard_detached.shape}"
        )
    
    # Reconstruct the full tensor using metadata
    all_tensors = []
    offset = 0
    for rank in range(world_size):
        shard_size = metadata_dict[rank][2]
        rank_shard_flattened = gathered[
            offset : offset + shard_size
        ]
        all_tensors.append(rank_shard_flattened)
        offset += shard_size

    all_tensors = trim_padding(all_tensors, rank, world_size, metadata_dict)

    concatenated = torch.cat(all_tensors)
    original_shape = metadata_dict[rank][1]
    return concatenated.reshape(original_shape)


def collectives_reduce_scatter(tensor, metadata_dict):
    """Reduce-scatter with even sharding. Returns local shard trimmed to original size."""
    rank = get_rank()
    world_size = get_size()

    original_numel, _, shard_size, padding = metadata_dict[rank]

    # Pad tensor if needed
    tensor_padded = tensor.reshape(-1)
    if padding > 0:
        tensor_padded = torch.concatenate([tensor_padded, torch.zeros(padding, device=tensor.device, dtype=tensor_padded.dtype)])

    tensor_padded = tensor_padded.contiguous()
    local_shard = torch.empty(shard_size, device=tensor.device, dtype=tensor_padded.dtype).contiguous()
    
    # Collective operation
    start = time.time()
    reduce_scatter(tensor_padded, local_shard)
    end = time.time()
    
    total_time = "{:.1e}".format(end - start)
    bandwidth = "{:.1e}".format(tensor_padded.nbytes / (end - start) / 1e9)
    logger.info(
        f"Reduce_scatter time on device {tensor.device if hasattr(tensor, 'device') else 'CPU'}: {total_time}, bandwidth: {bandwidth} GB/s"
    )

    # Trim padding on last rank using its original size from metadata_dict
    if rank == world_size - 1:
        valid_elements = original_numel - padding
        local_shard = local_shard[:valid_elements]

    return local_shard


class _AllGather(torch.autograd.Function):
    @staticmethod
    def forward(ctx, shard, metadata_dict):
        ctx.metadata_dict = metadata_dict
        return collectives_all_gather(shard, metadata_dict)

    @staticmethod
    def backward(ctx, grad_output):
        metadata_dict = ctx.metadata_dict
        return collectives_reduce_scatter(grad_output, metadata_dict), None


all_gather_op = _AllGather.apply
