#!/usr/bin/python3

"""
This a module defines a class Square with a private size attribute.
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size):
        """
        Initialize thr square with a given size.
        Size is private
        """
        self.__size = size
