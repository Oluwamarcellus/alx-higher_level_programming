#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    num_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    r_num = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if num_dict[roman_string[i]] >= num_dict[roman_string[i + 1]]:
                r_num += num_dict[roman_string[i]]
            else:
                r_num -= num_dict[roman_string[i]]
        else:
            r_num += num_dict[roman_string[i]]
    return r_num
