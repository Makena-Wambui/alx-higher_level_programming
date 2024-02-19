#!/usr/bin/python3

"""
This is the 100-my_int module.
It supplies one class: MyInt
"""


class MyInt(int):
    """
    This is the class, MyInt.

    It Inherits from: Class Int

    MyInt is a rebel.
    MyInt has == and != operators inverted

    Methods:
        __eq__
        __ne__
    """

    def __eq__(self, other):
        """
        This is the Equal Method.
        It compares two objects of the class MyInt.
        It uses the != operator.
        Returns true if they are not equal.
        It overwrites the __eq__ method from parent class, int.
        Performs __ne__ behavior
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        This is the NotEqual Method.
        It compares two objects of the class MyInt.
        It uses the == operator.
        Returns true if they are equal.
        It overwrites the __ne__ method from parent class, int.
        Performs __eq__ behavior
        """
        return super().__eq__(other)
