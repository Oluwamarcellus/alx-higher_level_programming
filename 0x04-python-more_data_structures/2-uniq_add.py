#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        reduced = reduce(lambda x, y: x + y, set(my_list))
        return reduced
