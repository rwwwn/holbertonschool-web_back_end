#!/usr/bin/env python3
"""
Module that defines measure_runtime to run 4 async comprehensions in parallel.
"""

import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times in parallel and measures runtime.
    Returns:
        Total runtime in seconds as a float.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
