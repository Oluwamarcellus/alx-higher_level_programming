#!/usr/bin/python3
"""
10-square module

"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle (9-rectangle.py)
    """

    def __init__(self, size):
        """
        initializing the object
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        computes the area of the Square

        """

        return self.__size ** 2

    def __str__(self):
        """
        computes the string of the class
        """

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
