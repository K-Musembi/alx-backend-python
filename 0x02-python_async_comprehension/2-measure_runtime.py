#!/usr/bin/env python3
"""parallel comprehensons function"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """parallel comprehensions"""
    start_time = time.time()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end_time = time.time()

    return end_time - start_time
