#!/usr/bin/python3
"""
This module contains the function read_file(filename="")
that reads a UTF-8 text file and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
