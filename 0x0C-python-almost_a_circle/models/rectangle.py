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

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="", file=sys.stdout)
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

    def update(self, *args, **kwargs):
        """
        public method that assigns an argument
        to each attribute:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """

        attr = ["id", "width", "height", "x", "y"]
        args = args
        kwargs = kwargs
        if args:
            for idx, elem in enumerate(args):
                if idx > 4:
                    break
                if idx == 0:
                    super().__init__(None if type(elem) is not int else elem)
                else:
                    self.validate(attr[idx], elem)
                    st = "_Rectangle__" + attr[idx]
                    setattr(self, st, elem)
        else:
            kw_items = kwargs.items()
            for key, value in kw_items:
                if key == "id":
                    super().__init__(None if type(value) is not int else value)
                else:
                    self.validate(key, value)
                    st = "_Rectangle__" + key
                    setattr(self, st, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of the object
        """

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
