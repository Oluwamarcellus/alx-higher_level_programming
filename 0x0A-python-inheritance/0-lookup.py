#!/usr/bin/python3
"""
0-lookup module
returns the list of available attributes and methods of an object

"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods
    of the obj(object)
    """

    return list(dir(obj))
