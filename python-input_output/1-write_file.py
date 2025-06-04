#!/usr/bin/python3
"""This module contains a function that writes a string with UTF-8 encoding."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8)."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
