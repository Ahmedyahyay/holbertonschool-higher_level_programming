#!/usr/bin/python3
"""Define a Rectangle class with instance counting."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0  # public class attribute

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): width of the rectangle (default 0)
            height (int): height of the rectangle (default 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width ensuring it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height ensuring it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter.

        If width or height is 0, perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the rectangle with '#'.

        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string representation to recreate the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message on deletion and decrement instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
