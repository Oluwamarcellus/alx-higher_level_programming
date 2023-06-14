#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list):
        if my_list:
            sumation = float(0)
            denom = 0
            for x, y in my_list:
                sumation += (x * y)
                denom += y
            return sumation / denom
        else:
            return 0
    else:
        return 0
