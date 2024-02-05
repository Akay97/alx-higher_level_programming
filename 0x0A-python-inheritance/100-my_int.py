#!/usr/bin/python3
"""
A simple module containing a class for representing an integer with inverted == and != operators.
"""


class MyInt(int):
    """
    A class representing an integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the equality (==) operator to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality (!=) operator to invert its behavior.
        """
        return super().__eq__(other)
