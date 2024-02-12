#!/usr/bin/python3
"""
the class Rectangle
"""


from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle with the specified width, height, x, y, and id.

        Parameters:
        - width: The width of the rectangle (positive integer).
        - height: The height of the rectangle (positive integer).
        - x: The x-coordinate of the rectangle (integer, default is 0).
        - y: The y-coordinate of the rectangle (integer, default is 0).
        - id: The id of the rectangle (integer, default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        - value: The value to set as the width (positive integer).
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        - value: The value to set as the height (positive integer).
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x-coordinate attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate attribute.

        Parameters:
        - value: The value to set as the x-coordinate (integer).
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-coordinate attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate attribute.

        Parameters:
        - value: The value to set as the y-coordinate (integer).
        """
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - The area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the rectangle with the character #.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Format: "[Rectangle] (<id>) <x>/<y> - <width>/<height>"
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the rectangle.

        *args: Positional arguments (no-keyworded arguments).
            1st argument: id attribute
            2nd argument: width attribute
            3rd argument: height attribute
            4th argument: x attribute
            5th argument: y attribute

        **kwargs: Keyworded arguments (key/value).
        Each key in this dictionary represents an attribute to the instance.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
        - A dictionary containing the attributes of the rectangle.
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
