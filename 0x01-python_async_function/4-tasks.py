#!/usr/bin/env python3

"""
Module: 4-tasks

Contains an asynchronous function for spawning multiple tasks.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns task_wait_random
    n times with specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = []

    async def run_task_wait_random():
        delay = await task_wait_random(max_delay)
        delays.append(delay)

    tasks = [run_task_wait_random() for _ in range(n)]

    await asyncio.gather(*tasks)

    return sorted(delays)
