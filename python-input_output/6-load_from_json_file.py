#!/usr/bin/python3
"""This module defines a function that creates an object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Parameters:
    filename: The path to the JSON file.

    Returns:
    A Python object (dict, list, etc.) created from the file's content.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
