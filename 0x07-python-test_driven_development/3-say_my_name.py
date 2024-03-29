#!/usr/bin/python3
"""
Prints a formatted name message.

This module defines the function `say_my_name` which prints a message in the
format "My name is <first name> <last name>".

Functions:
    say_my_name(first_name, last_name=""): Prints the formatted name message.

"""

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
