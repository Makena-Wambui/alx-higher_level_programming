#!/usr/bin/python3
"""
This is the 0-lookup module.
It supplies one function:
    lookup(obj)
"""


def lookup(obj):
    """
    This is the lookup function.

    It returns a list of all methods and
    attributes available
    to an object, obj.
    """
    return dir(obj)
