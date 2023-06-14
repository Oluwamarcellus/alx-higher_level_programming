#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        ele = ""
        highest = a_dictionary[list(a_dictionary.keys())[0]]
        for x in a_dictionary:
            if a_dictionary[x] > highest:
                ele = x
        return ele
    else:
        return None
