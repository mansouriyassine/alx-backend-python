#!/usr/bin/env python3
"""
Contains measure_runtime coroutine
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = asyncio.get_event_loop().time()

    return end_time - start_time
