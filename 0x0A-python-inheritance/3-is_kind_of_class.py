#!/usr/bin/python3

"""
This is the 3-is_kind_of_class module.

It supplies one function:
    is_kind_of_class

"""


def is_kind_of_class(obj, a_class):
    """
    Function: is_kind_of_class

    Returns True if object is an instance of,
    or if the object is an instance of a class,
    That inherits from,
    the specified class.
    Otherwise, False.
    """
    if isinstance(obj, a_class):
        return True

    return False
