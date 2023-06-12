#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        if not my_list:
            return []
        return [True if x % 2 == 0 else False for x in my_list]
