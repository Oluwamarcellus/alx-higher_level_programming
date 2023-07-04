#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing/ setting the private attributes"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        strn = ""
        for _ in range(self.__height):
            for _ in range(self.__width):
                strn += str(self.print_symbol)
            strn += "\n"
        return strn[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints message when an instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
