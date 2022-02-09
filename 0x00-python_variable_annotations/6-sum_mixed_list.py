#!/usr/bin/env python3
"""
Define and annotate the following variables with the specified values
"""

from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sum different types
    '''
    return sum(mxd_lst)
