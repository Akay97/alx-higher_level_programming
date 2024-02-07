#!/usr/bin/python3
"""
a function that inserts a line of text to a file, after each line containing a specific string
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of n rows.

    Parameters:
    - n: An integer representing the number of rows in the Pascal's triangle.

    Returns:
    - A list of lists representing Pascal's triangle of n rows.
    - An empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
