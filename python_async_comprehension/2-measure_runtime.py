#!/usr/bin/env python3
"""Measure the total runtime of async comprehensions run in parallel."""

import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of running 4 async_comprehension() calls in parallel."""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
