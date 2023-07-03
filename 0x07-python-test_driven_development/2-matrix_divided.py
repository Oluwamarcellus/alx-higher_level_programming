#!/usr/bin/python3
"""
matrix didision module
Divides the elements inside a matrix
return a new list of the divided matrix elements
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix list
    returns a new list
    """

    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"

    if not type(matrix) is list or not matrix:
        raise TypeError(err1)

    if not type(div) in [int, float]:
        raise TypeError(err3)

    if div == 0:
        raise ZeroDivisionError(err4)

    row_len = []
    for i in matrix:
        if not type(i) is list or not i:
            raise TypeError(err1)

        c_type = [type(j) in [int, float] for j in i]
        if not all(c_type):
            raise TypeError(err1)

        row_len.append(len(i))
        if not all([x == row_len[0] for x in row_len]):
            raise TypeError(err2)

    d = [[round(x / div, 2) for x in i] for i in matrix]
    return d
