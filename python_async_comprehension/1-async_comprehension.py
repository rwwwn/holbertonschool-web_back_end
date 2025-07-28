#!/usr/bin/env python3
"""Module with async_comprehension coroutine that collects random numbers."""

import asyncio
from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floats from async_generator using async comprehension.
    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [i async for i in async_generator()]
