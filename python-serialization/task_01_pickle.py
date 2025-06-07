#!/usr/bin/env python3
"""Module for serializing and deserializing a custom object using pickle."""

import pickle


class CustomObject:
    """
    A custom object that can be serialized and deserialized using pickle.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): The name of the file to save the object to.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject from a file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject or None: The loaded object or None on failure.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
