#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list):
        if idx < 0 or idx >= len(my_list) or not my_list:
            return my_list
        del my_list[idx]
        return my_list
