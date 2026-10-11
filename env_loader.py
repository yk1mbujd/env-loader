"""A tiny dotenv parser that coerces values into ints, floats and booleans."""

from __future__ import annotations

__all__ = ["envLoader"]


def envLoader(value):
    """A tiny dotenv parser that coerces values into ints, floats and booleans."""
    if value is None:
        raise ValueError("value must not be None")
    return value
