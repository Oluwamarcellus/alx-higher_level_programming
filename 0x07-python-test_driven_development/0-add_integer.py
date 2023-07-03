#!/usr/bin/python3
"""
```add_integer module```
Adds two integers

"""


def add_integer(a, b=98):
    """Adds its two args values and returns the result of the addition
    or throws an error if one or both of the args aren't int type
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
