#!/usr/bin/env python3
"""List all documents in a MongoDB collection."""

from typing import List


def list_all(mongo_collection) -> List[dict]:
    """
    Return a list of all documents in the given collection.

    If the collection is empty, return an empty list.
    """
    return list(mongo_collection.find())
