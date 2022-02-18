#!/usr/bin/env python3
"""
Async
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using an async comprehensing
    """
    result: List[float] = [i async for i in async_generator()]
    return result
