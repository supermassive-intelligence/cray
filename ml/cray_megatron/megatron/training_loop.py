from cray_megatron.megatron.dataset.data_loader import DataLoader

from cray_megatron.models.get_model_manager import get_model_manager
from cray_megatron.models.does_any_checkpoint_exist import does_any_checkpoint_exist
from cray_megatron.models.get_latest_checkpoint_path import get_latest_checkpoint_path

from cray_infra.training.training_job_status import TrainingJobStatus
from cray_infra.training.training_harness import TrainingHarness
from cray_infra.util.get_job_config import get_job_config

from torch.optim import AdamW

import torch

import os
import time
import logging

logger = logging.getLogger(__name__)


class TrainingLoop:
    def __init__(self, training_harness: TrainingHarness):
        self.training_harness = training_harness

        self.callbacks = get_callbacks(self)

        self.training_state = TrainingState()

    def train(self):
        try:
            self.model_manager = get_model_manager()
            self.training_state.model_info = self.model_manager.load_model()
        except Exception as e:
            import traceback

            error_message = (
                traceback.format_exc()
            )  # Capture the stack trace as a string
            print(f"An error occurred in loading the model: {error_message}")

        try:
            self.training_loop()
        except Exception as e:
            import traceback

            error_message = (
                traceback.format_exc()
            )  # Capture the stack trace as a string
            print(f"An error occurred in the training loop: {error_message}")

        self.checkpoint()

    def training_loop(self):
        import traceback

        try:
            self.on_train_begin()

            self.training_state.model_info["model"].train()

            max_steps = get_max_steps()

            self.training_state.optimizer = get_optimizer(
                self.training_state.model_info["model"]
            )
            self.training_state.scheduler = get_scheduler(
                self.training_state.optimizer, max_steps
            )

            if does_any_checkpoint_exist():
                self.resume_from_checkpoint()

            data_loader = DataLoader(
                model=self.training_state.model_info["model"],
                tokenizer=self.training_state.model_info["tokenizer"],
            )

            data_iterator = iter(data_loader)

            starting_step = self.training_state.current_step

            for step in range(starting_step, max_steps):
                self.training_state.current_step = step
                self.training_state.epoch = data_loader.epoch

                self.on_step_begin(step)

                batch = next(data_iterator)

                self.training_step(batch)

                self.on_step_end(step)

                if self.training_state.should_stop_training:
                    break

            self.on_train_end()
        except Exception as e:
            print("An error occurred:")
            traceback.print_exc()  # This will print the full stack trace
            # Optionally log the exception to a file for later review
            with open("error_log.txt", "a") as f:
                f.write("An error occurred:\n")
                traceback.print_exc(file=f)

    def resume_from_checkpoint(self):
        latest_checkpoint_path = get_latest_checkpoint_path()
        checkpoint = torch.load(latest_checkpoint_path, weights_only=True)

        self.training_state.current_step = checkpoint["step"]
        self.training_state.epoch = checkpoint["epoch"]
        self.training_state.model_info["model"].load_state_dict(
            checkpoint["model_state_dict"]
        )
        self.training_state.optimizer.load_state_dict(
            checkpoint["optimizer_state_dict"]
        )
        self.training_state.scheduler.load_state_dict(
            checkpoint["scheduler_state_dict"]
        )

        self.training_state.history = self.training_harness.get_status()["history"]

    def training_step(self, batch):

        device = self.training_state.model_info["distribution_strategy"]["device"]
        # forward pass
        loss = self.training_state.model_info["model"](
            input_ids=batch["input_ids"].to(device),
            attention_mask=batch["attention_mask"].to(device),
            labels=batch["labels"].to(device),
        ).loss

        logger.info(
            f"Training step {self.training_state.current_step} "
            f"- epoch {self.training_state.epoch} "
            f"- loss {loss.item()} "
            f"- learning rate {self.training_state.scheduler.get_last_lr()[0]}"
        )

        # backward pass
        self.training_state.optimizer.zero_grad()
        loss.backward()

        self.training_state.optimizer.step()
        self.training_state.scheduler.step()

        # log loss
        self.update_history(loss)

    def on_train_begin(self):
        self.training_state.start_time = time.time()
        for callback in self.callbacks:
            if hasattr(callback, "on_train_begin"):
                callback.on_train_begin()

    def on_step_begin(self, step):
        for callback in self.callbacks:
            if hasattr(callback, "on_step_begin"):
                callback.on_step_begin(step)

    def on_step_end(self, step):
        for callback in self.callbacks:
            if hasattr(callback, "on_step_end"):
                callback.on_step_end(step)

    def on_train_end(self):
        logger.info(
            f"Training finished successfully after {time.time() - self.training_state.start_time} seconds"
        )
        for callback in self.callbacks:
            if hasattr(callback, "on_train_end"):
                callback.on_train_end()

    def checkpoint(self):
        checkpoint = {
            "model_state_dict": filter_checkpoint(
                self.training_state.model_info["model"].state_dict()
            ),
            "optimizer_state_dict": self.training_state.optimizer.state_dict(),
            "scheduler_state_dict": self.training_state.scheduler.state_dict(),
            "step": self.training_state.current_step,
            "epoch": self.training_state.epoch,
        }

        checkpoint_name = f"checkpoint_{self.training_state.current_step}.pt"

        self.training_harness.checkpoint(
            model=self.training_state.model_info["model"],
            checkpoint_state=checkpoint,
            checkpoint_name=checkpoint_name,
        )

    def update_history(self, loss):
        job_config = get_job_config()

        max_history_length = job_config["training_history_length"]

        entry = {
            "step": self.training_state.current_step,
            "loss": loss.item(),
            "epoch": self.training_state.epoch,
            "time": time.time() - self.training_state.start_time,
        }

        self.training_state.history.append(entry)

        if len(self.training_state.history) > max_history_length:
            self.training_state.history = remove_closest_entry(
                self.training_state.history, max_history_length
            )

        self.training_harness.update_status(
            status=TrainingJobStatus.TRAINING,
            metadata={"history": self.training_state.history},
        )


def get_callbacks(trainer):
    return [
        TimeoutCallback(trainer),
        CheckpointCallback(trainer),
    ]


class TimeoutCallback:
    def __init__(self, trainer):
        job_config = get_job_config()
        self.timeout = job_config["timeout"]

    def on_train_begin(self):
        self.start_time = time.time()

    def on_step_end(self, step):
        if time.time() - self.start_time > self.timeout:
            logger.info(
                f"Training timed out after {time.time() - self.start_time} seconds"
            )
            self.training_state.should_stop_training = True


class CheckpointCallback:
    def __init__(self, trainer):
        self.trainer = trainer
        job_config = get_job_config()
        self.steps_per_checkpoint = job_config["steps_per_checkpoint"]

    def on_step_end(self, step):
        if step % self.steps_per_checkpoint == 0 and step != 0:
            start_time = time.time()
            self.trainer.checkpoint()
            logger.info(
                f"Checkpoint on step {step} took {time.time() - start_time} seconds"
            )


class TrainingState:
    def __init__(self):
        self.should_stop_training = False
        self.current_step = 0
        self.model_info = None
        self.optimizer = None
        self.scheduler = None
        self.history = []
        self.start_time = None


def get_max_steps():
    job_config = get_job_config()
    return job_config["max_steps"]


def get_optimizer(model):
    # use AdamW optimizer
    job_config = get_job_config()
    learning_rate = job_config["learning_rate"]
    return AdamW(model.parameters(), lr=learning_rate)


def get_scheduler(optimizer, max_steps):
    return torch.optim.lr_scheduler.LinearLR(
        optimizer,
        start_factor=1.0,
        end_factor=0.0,
        total_iters=max_steps,
    )


def remove_closest_entry(history, max_length):
    # The training history should include evenly spaced entries
    # up to the maximum length
    # Remove the most closely spaced entry to another entry
    # until the history is the correct length
    while len(history) > max_length:
        min_diff = float("inf")
        min_index = None
        for i in range(1, len(history) - 1):
            diff = history[i + 1]["step"] - history[i - 1]["step"]
            if diff < min_diff:
                min_diff = diff
                min_index = i
        history.pop(min_index)

    return history


def filter_checkpoint(state_dict):
    # Remove the layers without gradients
    return {k: v for k, v in state_dict.items() if v.requires_grad}
