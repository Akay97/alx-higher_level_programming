#!/usr/bin/python3
"""
A simple module containing classes for representing geometry.
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

    def integer_validator(self, name, value):
        """
        Validates the given value.

        Parameters:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with the specified width and height.

        Parameters:
        - width: The width of the rectangle (positive integer).
        - height: The height of the rectangle (positive integer).
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Format: "[Rectangle] <width>/<height>"
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
