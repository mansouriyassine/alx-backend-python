#!/usr/bin/env python3
    """
    Asynchronous generator coroutine that yields
    random numbers between 0 and 10.

    This coroutine loops 10 times, waiting for 1 second asynchronously
    on each iteration, and then yields a random floating-point number
    between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.

    Returns:
        AsyncGenerator[float, None]: An asynchronous
        generator object that yields random numbers.
    """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator coroutine that yields
    random numbers between 0 and 10.

    This coroutine loops 10 times, waiting for 1 second asynchronously
    on each iteration, and then yields a random floating-point number
    between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.

    Returns:
        AsyncGenerator[float, None]: An asynchronous
        generator object that yields random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
