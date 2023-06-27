#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Square classs"""
    def __init__(self, size=0):
        """initialization"""
        if type(size).__name__ != "int":
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
