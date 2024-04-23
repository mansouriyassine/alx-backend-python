#!/usr/bin/env python3
"""
Contains async_generator coroutine
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields random numbers between 0 and 10.
    Waits for 1 second before each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
