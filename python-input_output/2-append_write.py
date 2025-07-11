#!/usr/bin/python3
"""This module contains a function that appends text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
