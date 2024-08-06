#!/usr/bin/env python3
"""coroutines function"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay) -> List[float]:
    """spawn wait_random n times"""
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    results = await asyncio.gather(*tasks)

    n = len(results)
    for i in range(n):
        for j in range(0, n-i-1):
            if results[j] > results[j+1]:
                results[j], results[j+1] = results[j+1], results[j]
    return results
