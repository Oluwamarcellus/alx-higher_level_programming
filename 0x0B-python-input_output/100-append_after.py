#!/usr/bin/python3
"""
100-append_after
"""


import os


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r", encoding="utf-8") as old_f:
        with open("new.txt", "a", encoding="utf-8") as new_f:
            for o_file in old_f:
                new_f.write(o_file)
                if search_string in o_file:
                    new_f.write(new_string)
            os.remove(filename)
            os.rename("new.txt", filename)
