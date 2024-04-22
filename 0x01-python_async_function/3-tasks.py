#!/usr/bin/env python3

import asyncio
import random
from typing import List

async def task_wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for a
    random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

def task_wait_random_wrapper(max_delay: int) -> asyncio.Task:
    """
    Wrapper function that creates and returns
    an asyncio Task for task_wait_random.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio Task object.
    """
    return asyncio.create_task(task_wait_random(max_delay))