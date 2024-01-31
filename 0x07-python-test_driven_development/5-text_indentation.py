#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of the characters: ., ? and :.

This module defines the function `text_indentation` which prints a text with 2 new lines
after each occurrence of the characters '.', '?', and ':'.

Functions:
    text_indentation(text): Prints the text with 2 new lines after specified characters.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters: ., ? and :.

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n\n", end="")
