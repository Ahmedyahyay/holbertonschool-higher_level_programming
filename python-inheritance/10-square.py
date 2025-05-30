#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize the square with a validated size"""
        self.integer_validator("size", size)
        self.__size = size

        # Call Rectangle's __init__ with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
