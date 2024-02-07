#!/usr/bin/python3
"""
A module containing a function to load an object from a JSON file.
"""


import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
    - filename: The name of the JSON file to load from.

    Returns:
    - The object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
