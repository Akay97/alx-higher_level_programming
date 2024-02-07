#!/usr/bin/python3
"""
A module containing a function to append a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of characters added.

    Parameters:
    - filename: The name of the text file to append to (default: '').
    - text: The string to append to the file (default: '').

    Returns:
    - The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
