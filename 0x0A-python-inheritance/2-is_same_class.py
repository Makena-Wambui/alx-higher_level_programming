#!/usr/bin/python3

"""
This is the 2-is_same_class module.
It supplies one function:
    is_same_class
"""


def is_same_class(obj, a_class):
    """
    Function: is_same_class

    Return: True if obj is exactly an instance
    of a_class.

    Otherwise return false.
    """

    if type(obj) is a_class:
        return True

    return False
