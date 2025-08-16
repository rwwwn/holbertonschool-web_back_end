#!/usr/bin/env python3
"""Insert a new document in a MongoDB collection."""

from typing import Any, Dict


def insert_school(mongo_collection, **kwargs: Dict[str, Any]):
    """
    Insert a new document into the collection using kwargs.

    Returns the inserted document's _id.
    """
    res = mongo_collection.insert_one(dict(kwargs))
    return res.inserted_id
