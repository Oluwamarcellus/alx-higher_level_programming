#!/usr/bin/python3
"""
Rectangle module
"""

import sys
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        get width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        set width
        """

        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """
        get height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        set height
        """

        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """
        get x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        set x
        """

        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """
        get y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        set y
        """

        self.validate("y", value)
        self.__y = value

    @staticmethod
    def validate(attr, val):
        """
        setters attribute value validator
        """

        if type(val) != int:
            raise TypeError("{} must be an integer".format(attr))
        if attr == "x" or attr == "y":
            if val < 0:
                raise ValueError("{} must be >= 0".format(attr))
        elif val <= 0:
            raise ValueError("{} must be > 0".format(attr))

    def area(self):
        """
        Returns the area value of the Rectangle
        """

        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """

        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end="", file=sys.stdout)
            print()

    def __str__(self):
        """
        returns the string representation of the Rectangle
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        h = self.__height
        w = self.__width
        x = self.__x
        y = self.__y
        id_ = self.id
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id_, x, y, w, h)
