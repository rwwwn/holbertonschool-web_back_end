#!/usr/bin/env python3
"""
This module provides an async function that runs multiple
coroutines concurrently.
"""

import asyncio
from typing import List
from importlib import import_module

wait_random = import_module(
    '0-basic_async_syntax'
).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently and return the list
    of delays in ascending order.
    """
    tasks = (wait_random(max_delay) for _ in range(n))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
