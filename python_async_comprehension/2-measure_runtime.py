#!/usr/bin/env python3
"""
Measure the total runtime of 4 parallel comprehensions."""
import asyncio
import time
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of 4 parallel comprehensions."""
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
