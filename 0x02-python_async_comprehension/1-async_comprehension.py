#!/usr/bin/env python3
"""
Contains async_comprehension coroutine
"""

from typing import List

from random import uniform
from asyncio import gather

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.
    Returns a list of the 10 random numbers.
    """
    return [i async for i in async_generator()]
