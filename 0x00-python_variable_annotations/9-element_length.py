#!/usr/bin/env python3
"""
type-annotated
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return values with appropriate types
    """
    return [(i, len(i)) for i in lst]