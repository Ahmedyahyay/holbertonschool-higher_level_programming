#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of a class
or an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass thereof.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance or subclass instance of a_class, else False.
    """
    return isinstance(obj, a_class)
