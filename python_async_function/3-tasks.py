#!/usr/bin/env python3
"""
This module provides a function that returns an asyncio Task
for an asynchronous coroutine that waits for a random delay.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay time in seconds.

    Returns:
        asyncio.Task: The task object for the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
