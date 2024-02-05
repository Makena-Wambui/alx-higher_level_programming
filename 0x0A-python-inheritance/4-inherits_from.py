#!/usr/bin/python3

"""
This is the 4-inherits_from module.
It supplies one function: inherits_from
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object
    is an instance of a class that inherited (directly or indirectly)
    from the specified class;
    otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
