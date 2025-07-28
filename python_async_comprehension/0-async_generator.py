#!/usr/bin/env python3
"""Module that defines async_generator, a coroutine yielding 10 random numbers."""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random floats between 0 and 10, each after a 1 second delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
