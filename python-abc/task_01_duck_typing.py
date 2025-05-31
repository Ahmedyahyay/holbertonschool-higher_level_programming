#!/usr/bin/env python3
# Import ABC and abstractmethod from abc module
from abc import ABC, abstractmethod
# Import math for pi constant
import math


# Define the abstract base class Shape
class Shape(ABC):

    # Abstract method for calculating area
    @abstractmethod
    def area(self):
        pass

    # Abstract method for calculating perimeter
    @abstractmethod
    def perimeter(self):
        pass


# Define Circle class inheriting from Shape
class Circle(Shape):

    # Initialize with radius
    def __init__(self, radius):
        self.radius = radius

    # Calculate area of the circle
    def area(self):
        return math.pi * (self.radius ** 2)

    # Calculate perimeter (circumference) of the circle
    def perimeter(self):
        return 2 * math.pi * self.radius


# Define Rectangle class inheriting from Shape
class Rectangle(Shape):

    # Initialize with width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Calculate area of the rectangle
    def area(self):
        return self.width * self.height

    # Calculate perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)


# Define shape_info function using duck typing
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
