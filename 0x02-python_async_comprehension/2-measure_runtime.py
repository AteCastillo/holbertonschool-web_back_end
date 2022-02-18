#!/usr/bin/env python3
"""
Async
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes four times in parallel
    """
    start: float = time.time()
    func: List = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]
    await asyncio.gather(*func)
    end: float = time.time()

    return (end - start)