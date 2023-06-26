#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if my_list:
            for i in range(x):
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
            print()
    except IndexError:
        pass
