#!/usr/bin/python3
"""
models/square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, subclass of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the class
        """

        size = self.width
        id_ = self.id
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id_, x, y, size)

    @property
    def size(self):
        """
        getter function for size
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        setter function for size attribute
        """

        self.validate("width", value)
        self.width = value
        self.height = value

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

        attr = ["id", "width", "x", "y"]
        args = args
        kwargs = kwargs
        size = self.size
        x = self.x
        y = self.y
        if args:
            for idx, elem in enumerate(args):
                if idx > 3:
                    break
                if idx == 0:
                    id_v = None if type(elem) is not int else elem
                    super().__init__(size, size, x, y, id_v)
                else:
                    self.validate(attr[idx], elem)
                    st = "_Rectangle__" + attr[idx]
                    setattr(self, st, elem)
        else:
            kw_items = kwargs.items()
            for key, value in kw_items:
                if key == "id":
                    id_v = None if type(value) is not int else value
                    super().__init__(size, size, x, y, id_v)
                elif key in ["x", "y", "size"]:
                    if key == "size":
                        key = "width"
                    self.validate(key, value)
                    st = "_Rectangle__" + key
                    setattr(self, st, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """

        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y,
                }
