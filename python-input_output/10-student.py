#!/usr/bin/python3
"""Defines a Student class with selective JSON serialization."""


class Student:
    """Class that defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        Only includes attributes listed in `attrs` if it's
        a valid list of strings.
        """
        if (
            isinstance(attrs, list)
            and all(isinstance(item, str) for item in attrs)
        ):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        else:
            return self.__dict__
