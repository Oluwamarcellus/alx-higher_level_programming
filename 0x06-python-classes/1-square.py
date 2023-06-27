#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification)"""


class Square:
    """Square class"""
    def __init__(self, size):
        """Instantiation"""
        self.__size = size
