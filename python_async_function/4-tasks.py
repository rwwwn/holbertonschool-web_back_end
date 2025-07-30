#!/usr/bin/env python3
"""
This module defines a coroutine that spawns multiple asyncio Tasks
for concurrent waiting and returns their results in ascending order.
"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


Async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` asynchronous tasks using `task_wait_random`,
    each waiting for a random delay up to `max_delay`.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = (task_wait_random(max_delay) for _ in range(n))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
