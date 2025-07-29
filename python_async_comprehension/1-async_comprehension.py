#!/usr/bin/env python3
"""Coroutine that measures runtime of parallel async comprehensions."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]
