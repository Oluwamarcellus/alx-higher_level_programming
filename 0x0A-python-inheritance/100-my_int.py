#!/usr/bin/python3
"""
100-my_int module

"""


class MyInt(int):
    """
    class that inverts the '==' and '!=' functionality
    """

    def __eq__(self, other):
        """
        handles equality '==' operation
        """

        return not self.real == other.real

    def __ne__(self, other):
        """
        handles inequality '!=' operation
        """

        return not self.real != other.real
