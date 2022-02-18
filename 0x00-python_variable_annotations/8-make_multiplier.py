#!/usr/bin/env python3
"""
type-annotated 
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier argument, returns function that multiplies float
    """
    def function_multiplier(n: float) -> float:
        return (n * multiplier)
    return (function_multiplier)