#!/usr/bin/python3
"""
7-base_geometry module


"""


class BaseGeometry:
    """
    class BaseGeometry (based on 6-base_geometry.py)

    """

    def area(self):
        """
        Not defined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        string validator

        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
