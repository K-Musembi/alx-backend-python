#!/usr/bin/env python3
"""annotate function"""

from typing import List, Tuple, Any, Iterable


def element_length(lst: Iterable[Any]) -> List[Tuple[Any, int]]:
    """annotate variables"""
    return [(i, len(i)) for i in lst]
