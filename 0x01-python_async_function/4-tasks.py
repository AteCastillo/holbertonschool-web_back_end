#!/usr/bin/env python3
"""
Async/await and asyncio
"""
import asyncio
from typing import List, Any
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments
    """
    delay_list: List[float] = []
    result_list: List[Any] = []
    for _ in range(n):
        delay_list.append(task_wait_random(max_delay))
    for delay_task in asyncio.as_completed(delay_list):
        result_list.append(await delay_task)

    return (result_list)
