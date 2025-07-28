#!/usr/bin/env python3
"""
This module measures the average execution time per coroutine
when running wait_n concurrently.
"""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total runtime of wait_n(n, max_delay)
    and returns the average time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
