#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total_sum = 0

    for arg_str in sys.argv[1:]:
        total_sum += int(arg_str)

    print(total_sum)
