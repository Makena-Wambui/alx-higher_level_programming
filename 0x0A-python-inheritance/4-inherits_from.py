#!/usr/bin/python3

"""
This is the 4-inherits_from module.
It supplies one function:
    inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """
    Function: inherits_from(obj, a_class):

    Returns true if obj belongs to a class that inherited directly
    or indirectly from a_class.

    Otherwise: False
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True

    return False
