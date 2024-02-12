#!/usr/bin/python3
"""
Write the first class Base
"""


class Base:
    """
    Base class to manage id attribute for other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Parameters:
        - id: An optional integer representing the id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
