#!/usr/bin/python3
"""
Module to check if an object is an instance of a class that inherits (directly or indirectly)
from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherits from a_class
    (but not if obj is exactly an instance of a_class).

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance against.

    Returns:
        True if obj's class inherits from a_class, False otherwise.
    """
    # Check if obj is instance of a_class or subclass, but exclude exact class match
    return issubclass(type(obj), a_class) and type(obj) is not a_class
