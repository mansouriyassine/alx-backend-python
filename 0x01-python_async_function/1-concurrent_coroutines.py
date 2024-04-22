#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random
    n times with specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = []

    async def run_wait_random():
        delay = await wait_random(max_delay)
        delays.append(delay)

    tasks = [run_wait_random() for _ in range(n)]

    await asyncio.gather(*tasks)

    return sorted(delays)