#!/usr/bin/python3
"""
This module contains an object represented by
JSON string
""""

def from_json_string(my_str):
"""Function returns an object represented by JSON string"""

    return json.loads(my_str)
