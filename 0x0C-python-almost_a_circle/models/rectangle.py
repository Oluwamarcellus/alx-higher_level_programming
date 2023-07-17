#!/usr/bin/python3
"""
models/rectangle module


"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width attr getter function
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        width attr setter function
        """

        self.__width = value

    @property
    def height(self):
        """
        the getter function of height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter funct for height
        """

        self.__height = value

    @property
    def x(self):
        """
        x getter function
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter function
        """

        self.__x = value

    @property
    def y(self):
        """
        y getter function
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter function
        """

        self.__y = value
