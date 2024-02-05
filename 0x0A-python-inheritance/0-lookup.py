#!/usr/bin/python3
"""
This is the 0-lookup module.
It supplies one function: lookup
"""


def lookup(obj):
    """
    This is the lookup function.
    It returns the list of available attributes and methods of an object
    Returns a list object
    """
    return dir(obj)
