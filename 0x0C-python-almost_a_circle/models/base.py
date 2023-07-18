#!/usr/bin/python3
"""
models/base module


"""


import json
import os


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """

        c_name = cls.__name__
        with open(c_name + ".json", "w", encoding="utf-8") as f:
            if list_objs is None or list == []:
                f.write("[]")
            else:
                jslist = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(jslist))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """

        f_name = cls.__name__ + ".json"
        if not os.path.exists(f_name):
            return []
        with open(f_name, "r", encoding="utf-8") as f:
            j_file = Base.from_json_string(f.read())
            return [cls.create(**i) for i in j_file]
