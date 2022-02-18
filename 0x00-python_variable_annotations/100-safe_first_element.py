#!/usr/bin/env python3
"""
type-annotated function.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    return values with appropriate types
    """
    if lst:
        return lst[0]
    else:
        return None