#!/usr/bin/env python3
"""This module defines a function that returns a key-value tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of an int or float."""
    return (k, float(v ** 2))
