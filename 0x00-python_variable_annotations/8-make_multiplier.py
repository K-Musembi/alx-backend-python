#!/usr/bin/env python3
"""callable function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function"""
    return lambda x: multiplier * x
