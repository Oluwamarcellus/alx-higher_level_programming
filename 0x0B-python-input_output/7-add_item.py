#!/usr/bin/python3
"""
7-add_item

script that adds all arguments to a Python list, and
then save them to a file
"""


import sys


if __name__ == "__main__":
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file

    try:
        my_set = load("add_item.json")
    except Exception:
        my_set = []
    my_set = my_set + sys.argv[1:]
    save(my_set, "add_item.json")
