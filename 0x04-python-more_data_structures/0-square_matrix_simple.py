#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        squared = list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
        return squared
