#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize the square with a validated size"""
        self.integer_validator("size", size)
        self.__size = size

        # Call the Rectangle initializer with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
