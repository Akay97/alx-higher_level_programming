#!/usr/bin/python3
"""
Base module.
"""

import json
import csv

class Base:
    """
    Base class for managing id attribute in all classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with an optional id.

        Args:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary representing attributes.

        Returns:
            Base: An instance of the class with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file.

        The filename must be: <Class name>.json
        If the file doesn’t exist, return an empty list.
        Otherwise, return a list of instances - the type of these instances depends on cls.

        Returns:
            list: A list of instances loaded from a JSON file.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode='r', encoding='utf-8') as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to a CSV file.

        Args:
            list_objs (list): A list of instances to be serialized.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file.

        Returns:
            list: A list of instances deserialized from the CSV file.
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, mode='r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instances.append(cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])))
                    elif cls.__name__ == "Square":
                        instances.append(cls(int(row[0]), int(row[1]), int(row[2]), int(row[3])))
                return instances
        except FileNotFoundError:
            return []


