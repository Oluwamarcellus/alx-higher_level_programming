#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        if value not in a_dictionary.values():
            return a_dictionary
        for i in a_dictionary.copy():
            if a_dictionary[i] == value:
                del a_dictionary[i]
        return a_dictionary
    else:
        return None
