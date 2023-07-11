#!/usr/bin/python3
"""
7-add_item

script that adds all arguments to a Python list, and
then save them to a file
"""


import sys


save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


my_list = [i for i in sys.argv[1:]]


save(my_list, "add_item.json")


my_set = load("add_item.json")
