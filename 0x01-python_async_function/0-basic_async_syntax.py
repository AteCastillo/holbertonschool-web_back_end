#!/usr/bin/env python3
"""
Async/await and asyncio coroutines
"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
    Takes an integer that waits for a random delay and returns it
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)
