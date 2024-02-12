#!/usr/bin/python3
"""
the class Square
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Class Square inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square with the specified size, x, y, and id.

        Parameters:
        - size: The size of the square (positive integer).
        - x: The x-coordinate of the square (integer, default is 0).
        - y: The y-coordinate of the square (integer, default is 0).
        - id: The id of the square (integer, default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value: The value to set as the size (positive integer).
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.

        Format: "[Square] (<id>) <x>/<y> - <size>"
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the square.

        *args: Positional arguments (no-keyworded arguments).
            1st argument: id attribute
            2nd argument: size attribute
            3rd argument: x attribute
            4th argument: y attribute

        **kwargs: Keyworded arguments (key/value).
        Each key in this dictionary represents an attribute to the instance.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
        - A dictionary containing the attributes of the square.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
