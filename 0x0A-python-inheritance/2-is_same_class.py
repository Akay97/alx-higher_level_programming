#!/usr/bin/python3
"""
A simple module containing a function for checking if an object is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise, returns False.

    Parameters:
    - obj: Any object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
