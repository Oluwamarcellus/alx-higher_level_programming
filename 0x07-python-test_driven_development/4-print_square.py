#!/usr/bin/python3
"""
4-print_square Module
prints a square with the character #
Returns nothing
"""


def print_square(size):
    """function that prints a square with the character '#'
    L * B (size * size)
    """

    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        for j in range(size):
            print("#", end="" if j != size - 1 else "\n")
