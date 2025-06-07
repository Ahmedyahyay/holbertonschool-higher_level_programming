#!/usr/bin/python3
"""This module provides a function to convert a class
 instance into a JSON-serializable dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of an object
 for JSON serialization."""
    return obj.__dict__
