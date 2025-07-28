#!/usr/bin/env python3
"""Coroutine that measures runtime of parallel async comprehensions."""

import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measure total runtime of running async_comprehension 4 times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
