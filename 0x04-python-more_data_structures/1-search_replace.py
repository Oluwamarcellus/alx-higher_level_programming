#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        new_list = list(map(lambda x: x if x != search else replace, my_list))
        return new_list
