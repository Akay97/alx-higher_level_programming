#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Parameters:
    - obj: An instance of a class.

    Returns:
    - A dictionary representing the serializable attributes of the object.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
