#!/usr/bin/env python3
"""Define a class CountedIterator that counts how many items have been iterated"""

class CountedIterator:
    def __init__(self, iterable):
        """Initialize with an iterator and a counter"""
        self.iterator = iter(iterable)  # Store the iterator
        self.count = 0  # Initialize counter

    def __next__(self):
        """Return the next item and increment the counter"""
        item = next(self.iterator)  # Get the next item from the iterator
        self.count += 1  # Increment the counter
        return item

    def get_count(self):
        """Return the number of items iterated"""
        return self.count
