#!/usr/bin/python3
"""Function to return Pascal's triangle as a list of lists."""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for row_num in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
