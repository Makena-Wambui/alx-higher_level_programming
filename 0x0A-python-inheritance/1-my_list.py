#!/usr/bin/python3
"""
This is the 1-my_list module.
It supplies the class MyList,
which inherits from list and contains
one function, print_sorted.
"""

class MyList(list):
    """
    This is class: MyList
    It inherits from the class list
    Methods:
        print_sorted
    """
    def print_sorted(self):
        """
        This is a public instance method.
        It prints a list, in ascending order.
        """
        print(sorted(self))
