#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        reduced = sum(set(my_list))
        return reduced
