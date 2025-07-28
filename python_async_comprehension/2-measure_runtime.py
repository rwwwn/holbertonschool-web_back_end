#!/usr/bin/env python3
"""
Module that defines measure_runtime, which runs async_comprehension four times in parallel.
"""
import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Measures runtime for executing async_comprehension 4 times in parallel.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
