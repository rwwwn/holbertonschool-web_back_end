#!/usr/bin/env python3
"""Update topics of a school document by name."""

from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """
    Update all documents matching the given school name to set topics.

    Args:
        mongo_collection: The pymongo collection object.
        name: School name to match.
        topics: List of topic strings to set.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
