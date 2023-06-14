#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if isinstance(set_1, set) and isinstance(set_2, set):
        same = set_1.intersection(set_2)
        common = set_1.union(set_2)
        for i in same:
            common.remove(i)
        return common
