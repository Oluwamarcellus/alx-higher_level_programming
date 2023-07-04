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

    def area(self):
        """returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """string representation of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        str = ""
        for _ in range(self.__height):
            for _ in range(self.__width):
                str += "#"
            str += "\n"
        return str[:-1]
