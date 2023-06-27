#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initialization"""
        if type(size) != int:
            raise TypeError("must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            list(map(lambda x: list(map(lambda x: 
                print("#", end=("" if x != self.__size - 1 else "\n"))
                , range(self.__size))), range(self.__size)))
