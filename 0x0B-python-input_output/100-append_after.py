#!/usr/bin/python3
"""
a function that inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Parameters:
    - filename: A string representing the name of the file.
    - search_string: A string representing the search string.
    - new_string: A string representing the line to insert after each occurrence of the search string.

    Returns:
    - None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
