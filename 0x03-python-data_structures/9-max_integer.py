#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if not my_list:
            return None
        max = 0
        for x in my_list:
            if x > max:
                max = x
        return max
