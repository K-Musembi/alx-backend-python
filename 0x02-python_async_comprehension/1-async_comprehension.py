#!/usr/bin/env python3
"""async comprehension function"""

import asyncio
from typing import Iterator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterator[float]:
    """async comprehension"""
    numbers = [i async for i in async_generator()]

    return numbers
