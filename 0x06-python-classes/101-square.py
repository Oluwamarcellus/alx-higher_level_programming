#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization"""
        if type(size) != int:
            raise TypeError("must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        siz = self.__size
        pos = self.__position
        if siz == 0:
            print()
        else:
            if pos[1] > 0:
                print()
            for i in range(siz):
                [print(" ", end="") for x in range(pos[0])]
                [print("#", end="") for y in range(siz)]
                print()
