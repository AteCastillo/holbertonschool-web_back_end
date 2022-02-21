#!/usr/bin/env python3
"""
Return tuple of of size two
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return tuple of of size two containing a start index
    and an end index
    """
    index_end = (page * page_size)
    index_start = (index_end - page_size)
    index = index_start, index_end

    return index
