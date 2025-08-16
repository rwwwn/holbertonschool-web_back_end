#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

Ensures that when rows are removed between requests, clients do not miss
items while paging forward using indices.
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset (skip header row)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return a dict mapping original positional index -> row.

        We index the full dataset to match the provided examples.
        """
        if self.__indexed_dataset is None:
            data = self.dataset()
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page starting from `index`.

        Returns:
          {
            "index": start_index_used,
            "next_index": index_to_request_next,
            "page_size": returned_page_length,
            "data": page_rows
          }
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        max_key = max(indexed.keys()) if indexed else -1
        assert index <= max_key

        data: List[List] = []
        cursor = index

        # Collect up to page_size existing rows, skipping deleted keys.
        while len(data) < page_size and cursor <= max_key:
            if cursor in indexed:
                data.append(indexed[cursor])
            cursor += 1

        next_index = cursor
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
