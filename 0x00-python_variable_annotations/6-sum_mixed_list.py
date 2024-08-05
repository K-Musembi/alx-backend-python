#!/usr/bin/env python3
"""mixed list function"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """sum of mixed type list"""
    sum = 0.00
    if len(mxd_lst) > 0:
        for item in mxd_lst:
            sum += item

    return sum
