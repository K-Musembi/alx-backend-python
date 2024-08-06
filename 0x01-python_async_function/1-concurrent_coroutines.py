#!/usr/bin/env python3
"""coroutines function"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay):
    """spawn wait_random n times"""
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    results = await asyncio.gather(*tasks)

    return bubble_sort(results)


def bubble_sort(arr):
    """sort list"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
