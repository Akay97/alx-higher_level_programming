#!/usr/bin/python3


import math

class MagicClass:
    """
    This class represents MagicClass.

    Attributes:
    - __radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass class.

        Args:
        - radius (float, optional): The radius of the circle. Defaults to 0.
        """
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
        - float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
        - float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
