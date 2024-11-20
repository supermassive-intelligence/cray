import torch
from typing import Optional, Tuple
import torch.nn as nn
from transformers.models.llama.modeling_llama import LlamaDecoderLayer
from transformers.models.llama.configuration_llama import LlamaConfig 
from tokenformer.llama_tokenformer_attention import LlamaTokenformerAttention
from transformers.cache_utils import Cache

class LlamaTokenformerDecoderLayer(LlamaDecoderLayer):
    def __init__(self, config: LlamaConfig, layer_idx: int):
        super().__init__(config, layer_idx)
        self.self_attn = LlamaTokenformerAttention(config, layer_idx)
        self.ffn_tokenformer_key = nn.Parameter(torch.randn(config.hidden_size, config.hidden_size))
        self.ffn_tokenformer_value = nn.Parameter(torch.zeros(config.hidden_size, config.hidden_size))
        
    def forward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        past_key_value: Optional[Cache] = None,
        output_attentions: Optional[bool] = False,
        use_cache: Optional[bool] = False,
        cache_position: Optional[torch.LongTensor] = None,
        position_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = None, 
        **kwargs,
    ) -> Tuple[torch.FloatTensor, Optional[Tuple[torch.FloatTensor, torch.FloatTensor]]]:
        
        residual = hidden_states
        hidden_states = self.input_layernorm(hidden_states)

        # Tokenformer Attention
        hidden_states, tokenformer_attn_weights, present_key_value = self.self_attn(
            hidden_states=hidden_states,
            attention_mask=attention_mask,
            position_ids=position_ids,
            past_key_value=past_key_value,
            output_attentions=output_attentions,
            use_cache=use_cache,
        )
        hidden_states = residual + hidden_states

        # Fully Connected
        residual = hidden_states
        hidden_states = self.post_attention_layernorm(hidden_states)

        # Save hidden_states to use in tokenformer_attention
        ffn_input_hidden_states = hidden_states
        
        hidden_states = self.mlp(hidden_states)
        
        tokenformer_hidden_states = torch.nn.functional.scaled_dot_product_attention(
            ffn_input_hidden_states, self.ffn_tokenformer_key, self.ffn_tokenformer_value,
            is_causal=False # should be false for tokenformer
        )
        
        hidden_states = residual + hidden_states + tokenformer_hidden_states

        outputs = (hidden_states,)

        if output_attentions:
            outputs += (tokenformer_attn_weights,)

        if use_cache:
            outputs += (present_key_value,)

        return outputs