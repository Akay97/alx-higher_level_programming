#!/usr/bin/python3
"""
A simple module containing a function for checking if an object is an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, returns False.

    Parameters:
    - obj: Any object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
