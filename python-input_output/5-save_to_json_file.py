#!/usr/bin/python3
"""This module defines a function that writes a Python object
 to a text file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Parameters:
    my_obj (any): The Python object to serialize (list, dict, etc.)
    filename (str): The name of the file to write the JSON string into
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
