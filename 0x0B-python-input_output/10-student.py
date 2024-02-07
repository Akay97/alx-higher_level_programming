#!/usr/bin/python3
"""
a class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """
    A class to represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student with first name, last name, and age.

        Parameters:
        - first_name: A string representing the first name of the student.
        - last_name: A string representing the last name of the student.
        - age: An integer representing the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs: A list of strings representing attribute names.
                 If provided, only attributes contained in this list are retrieved.
                 If not provided or None, all attributes are retrieved.

        Returns:
        - A dictionary representing the selected attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
