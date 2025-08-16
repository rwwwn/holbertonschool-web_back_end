#!/usr/bin/env python3
"""
Hypermedia pagination (HATEOAS-style metadata) for the baby names dataset.
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple (start, end) for the items of a list on a given page.
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset (skip header row)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the rows for a given page, or an empty list if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return a hypermedia pagination descriptor for the requested page.

        Keys:
          page_size, page, data, next_page, prev_page, total_pages
        """
        data = self.get_page(page, page_size)
        total_items: int = len(self.dataset())
        if page_size:
            total_pages: int = math.ceil(total_items / page_size)
        else:
            total_pages = 0

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        page_len = len(data)

        return {
            "page_size": page_len,
            "page": page,
            "data": data,
            "next_page": next_page if page_len > 0 else None,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
