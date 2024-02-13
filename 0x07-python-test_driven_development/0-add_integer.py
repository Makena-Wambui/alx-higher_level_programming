#!/usr/bin/python3
"""This is the 0-add_integer module.
This module supplies the add function,
which adds two integers together.
"""


def add_integer(a, b=98):
    """
    This function returns the sum of two integers.
    a and b must be integers or floats.
    a and b must be first casted to integers if they are floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # a and b must be first casted to integers if they are float
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
