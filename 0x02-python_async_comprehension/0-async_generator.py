#!/usr/bin/env python3
"""coroutine function"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """yield random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
