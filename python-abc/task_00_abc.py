#!/usr/bin/python3
"""Define abstract class Animal and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class that implements the sound method."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that implements the sound method."""

    def sound(self):
        return "Meow"
