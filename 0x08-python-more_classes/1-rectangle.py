#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing/ setting the private attributes"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the width private attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """setting the value of width private attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieving the height private attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of height private attribute"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
