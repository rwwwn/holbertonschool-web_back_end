#!/usr/bin/env python3
"""
Write a type-annotated function task_wait_n that takes"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for n tasks to complete and returns a list of their delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    time_waits = await asyncio.gather(*tasks)
    return sorted(time_waits)
