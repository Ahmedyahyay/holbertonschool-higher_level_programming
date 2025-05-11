#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Load the compiled Python module
    from hidden_4 import *

    # Get the list of all names in the module
    names = dir()

    # Filter names that don't start with '__'
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort the filtered names
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)
