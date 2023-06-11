#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        new_str = ""
        for c in my_string:
            if c not in "cC":
                new_str += c
        return new_str
