#!/usr/bin/env python3
"""
Simple helper to compute start/end indices for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple (start, end) for the items of a list on a given page.

    Page numbers are 1-indexed. For example, page=1 and page_size=7
    returns (0, 7).
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)
