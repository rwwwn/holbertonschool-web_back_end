#!/usr/bin/env python3
"""This module defines a function that creates a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    return lambda x: x * multiplier
