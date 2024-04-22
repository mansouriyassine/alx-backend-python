#!/usr/bin/env python3

import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per operation.

    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time per operation.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n