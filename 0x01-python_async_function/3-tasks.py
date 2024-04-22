#!/usr/bin/env python3

import asyncio
from typing import Generator


async def wait_random(max_delay: int) -> float:
    """
    Wait for a random delay between 0 and `max_delay` seconds.
    """
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Generator[asyncio.Task, None, None]:
    """
    Create and return an asyncio.Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
