#!/usr/bin/python3
"""
A module containing a function to read and print the contents of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Parameters:
    - filename: The name of the text file to read (default: '').

    Returns:
    - None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
