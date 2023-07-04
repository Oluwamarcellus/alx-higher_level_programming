#!/usr/bin/python3
def magic_string():
    magic_string.my_attr = getattr(magic_string, "my_attr", 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.my_attr)])
