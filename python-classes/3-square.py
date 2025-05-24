#!/usr/bin/python3
"""Defines a Square class with a private size and area method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private attribute

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
