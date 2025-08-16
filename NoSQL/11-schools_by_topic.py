#!/usr/bin/env python3
"""Find schools by a specific topic."""

from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List[dict]:
    """
    Return the list of schools that have the given topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: Topic string to match inside the 'topics' field.
    """
    return list(mongo_collection.find({"topics": topic}))
