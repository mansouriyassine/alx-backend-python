#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments."""

import asyncio
import random
from typing import Generator


async def async_generator():
    """Asynchronous generator that yields random numbers between 0 and 10.
    Waits for 1 second before each yield."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)