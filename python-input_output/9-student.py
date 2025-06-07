#!/usr/bin/python3
"""Defines a class Student with public attributes and a JSON
 representation method."""


class Student:
    """A class that defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance."""
        return self.__dict__
