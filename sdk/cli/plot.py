from masint.util.make_api_url import make_api_url

import matplotlib.pyplot as plt

import aiohttp
import asyncio

import logging

logger = logging.getLogger(__name__)


def plot(model_name):
    logger.info(f"Plotting model {model_name}")

    try:
        asyncio.run(plot_async(model_name=model_name))
    except Exception as e:
        logger.error(f"Failed to plot model {model_name}")
        logger.error(e)


async def plot_async(model_name):
    status = await get_status(model_name)

    history = status["job_status"]["history"]
    model_name = clip_model_name(status["model_name"])

    # Plot loss against step
    plot_loss(history, model_name)


def plot_loss(history, model_name):
    steps = [int(entry["step"]) for entry in history]
    losses = [float(entry["loss"]) for entry in history]

    plt.plot(steps, losses)
    plt.xlabel("Step")
    plt.ylabel("Loss")
    plt.title("Training loss for model " + model_name)
    plt.grid(True)

    path = f"/app/cray/data/loss_plot_{model_name}.pdf"

    logger.info(f"Saving plot to {path}")

    plt.savefig(path)


async def get_status(model_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(make_api_url(f"v1/megatron/train/{model_name}")) as resp:
            data = await resp.json()

            logger.info(f"Got status for model {model_name}")
            logger.info(data)

            if resp.status != 200:
                logger.error(f"Failed to get status for model {model_name}")
                logger.error(data)
                raise Exception("Failed to get status for model")

            return data


def clip_model_name(model_name):
    return model_name[:10]
