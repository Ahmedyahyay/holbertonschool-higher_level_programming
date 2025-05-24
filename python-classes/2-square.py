#!/usr/bin/python3
"""Defines a Square class with private size attribute."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): Size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
