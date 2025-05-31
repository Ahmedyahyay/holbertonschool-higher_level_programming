#!/usr/bin/python3
"""Module defining a custom list class VerboseList that logs operations."""

class VerboseList(list):
    """Custom list class that prints messages on modifications."""

    def append(self, item):
        """Add item to the list and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print a message indicating how many items were added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Print a message before removing the item from the list."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print a message before popping an item from the list."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
