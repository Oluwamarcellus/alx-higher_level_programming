#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initialization"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
