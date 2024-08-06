#!/usr/bin/env python3
"""random delay function"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait for max_delay seconds"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
