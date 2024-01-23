#!/usr/bin/python3
"""square module."""


class Square:
    """
    This class represents a square.

    Attributes:
    - __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (float or int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
        - value (float or int): The size to set.

        Raises:
        - TypeError: If size is not a number (float or integer).
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Defines the equality comparison for the square based on area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Defines the inequality comparison for the square based on area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Defines the greater than comparison for the square based on area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Defines the greater than or equal comparison for the square based on area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Defines the less than comparison for the square based on area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Defines the less than or equal comparison for the square based on area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
