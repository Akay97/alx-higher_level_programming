#!/usr/bin/python3
"""
A simple module containing a base class for representing geometry.
"""


class BaseGeometry:
    """
    A class representing the base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
