#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    Returns False if the object is an instance of the class itself.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True or False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
