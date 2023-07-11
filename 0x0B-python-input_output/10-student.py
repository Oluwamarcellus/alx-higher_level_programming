#!/usr/bin/python3
"""
10-student module

"""


class Student:
    """
    class Student that defines a student by:
    ---- first_name
    ---- last_name
    ---- age

    """

    def __init__(self, first_name, last_name, age):
        """
        initializing the class instance/ object
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student isinstance
        """

        a = attrs
        if a and type(a) is list and all([type(i) is str for i in a]):
            return {x: getattr(self, x) for x in a if x in self.__dict__}
        return self.__dict__
