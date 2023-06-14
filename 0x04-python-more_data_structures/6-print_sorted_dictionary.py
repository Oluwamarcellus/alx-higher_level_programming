#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        for i in sorted(a_dictionary.keys()):
            print(f"{i}: {a_dictionary[i]}")
