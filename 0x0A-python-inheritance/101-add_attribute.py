#!/usr/bin/python3
"""
A simple module containing a function to add a new attribute to an object.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    - obj: The object to which the attribute should be added.
    - attribute: The name of the attribute to be added.
    - value: The value of the attribute.

    Raises:
    - TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
