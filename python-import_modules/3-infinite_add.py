#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Initialize the sum variable
    total = 0
    # Iterate through the arguments (starting from index 1 to skip the script name)
    for arg in sys.argv[1:]:
        total += int(arg)
    # Print the total sum
	print (total)
