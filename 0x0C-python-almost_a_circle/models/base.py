#!/usr/bin/python3
"""
models/base module


"""


import json


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
