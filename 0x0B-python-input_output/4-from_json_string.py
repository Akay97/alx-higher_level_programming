#!/usr/bin/python3
"""
A module containing functions to convert JSON strings to Python objects and vice versa.
"""


import json

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Parameters:
    - my_str: The JSON string to be converted.

    Returns:
    - A Python object represented by the JSON string.
    """
    return json.loads(my_str)
