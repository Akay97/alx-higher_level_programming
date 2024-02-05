#!/usr/bin/python3
"""
A simple module containing a function to look up and return a list of attributes of an object, excluding methods.
"""


def lookup(obj):
    """
    Returns a list of attributes of the given object, excluding methods.

    Parameters:
    - obj: Any object whose attributes and methods need to be looked up.

    Returns:
    - A list containing attribute names of the object.
    """
    return [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
