#!/usr/bin/env python3
"""
Async/await and asyncio coroutines
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes 2 int arguments and spawn
    """
    delay_list: List[float] = []
    result_list: List[float] = []
    for _ in range(n):
        delay_list.append(asyncio.create_task(wait_random(max_delay)))
    for delay_task in asyncio.as_completed(delay_list):
        result_list.append(await delay_task)

    return (result_list)