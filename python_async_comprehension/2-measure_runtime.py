#!/usr/bin/env python3
"""Coroutine to measure total runtime of parallel async comprehensions."""
import asyncio
import time
from 1-async_comprehension import async_comprehension  # adjust if needed

async def measure_runtime() -> float:
    """
    Runs async_comprehension 4 times in parallel and measures total runtime.
    Returns:
        float: Total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
