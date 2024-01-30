#!/usr/bin/python3
"""
Prints a square with the character #.

This module defines the function `print_square` which prints a square of '#' characters.

Functions:
    print_square(size): Prints the square with the specified size.

"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): Size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
