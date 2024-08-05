#!/usr/bin/env python3
"""tuple function"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """string and int/float to tuple"""
    my_tup: Tuple[str, float] = (k, v * v)
    return my_tup
