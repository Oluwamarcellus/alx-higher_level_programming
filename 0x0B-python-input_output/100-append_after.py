#!/usr/bin/python3
"""
100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    
    txt = ""
    with open(filename, "r", encoding="utf-8") as f:
        for i in f:
            txt += i
            if search_string in i:
                txt += new_string

    with open(filename, "w", encoding="utf-8") as new_f:
        new_f.write(txt)
