#!/usr/bin/python3
"""
A module containing a function to write a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Parameters:
    - filename: The name of the text file to write to (default: '').
    - text: The string to write to the file (default: '').

    Returns:
    - The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
