#!/usr/bin/env python3
"""list annotation function"""


def sum_list(input_list: list[float]) -> float:
    """sum of list"""
    sum = 0
    if len(input_list) > 0:
        for item in input_list:
            sum += item

    return sum
