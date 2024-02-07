#!/usr/bin/python3
"""
A module containing a function to convert an object to its JSON representation.
"""


import json

def to_json_string(my_obj):
    """
    Converts an object to its JSON representation.

    Parameters:
    - my_obj: The object to be converted.

    Returns:
    - A JSON string representing the object.
    """
    return json.dumps(my_obj)
