#!/usr/bin/python3
"""
Module 2-is_same_class

This module provides a function that checks if an object is exactly
an instance of the specified class (not a subclass).
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if type(obj) is exactly a_class, False otherwise.
    """
    return type(obj) is a_class
