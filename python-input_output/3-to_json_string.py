#!/usr/bin/python3
"""
This module contains a function that returns
the JSON representation of an object (as a string).
"""

import json  # Used to convert Python objects to JSON strings


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj (any): The Python object to be converted

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
