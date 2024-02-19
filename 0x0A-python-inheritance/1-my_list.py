#!/usr/bin/python3

"""
This is the 1-my_list module.
It supplies one class:
    MyList.
"""


class MyList(list):
    """
    This is the class MyList.
    It inherits from the class list.

    Methods:
        print_sorted

    """
    def print_sorted(self):
        """
        Method: print_sorted
        Prints a sorted list of ints.
        """
        print(sorted(self))
