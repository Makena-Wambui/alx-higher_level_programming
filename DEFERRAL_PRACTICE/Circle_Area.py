#!/usr/bin/python
from math import pi
"""This is the Circle_Area module.
It contains one function, Area which computes the
area of a circle of radius, r.
"""


def Area(r):
    """This function returns the area of a circle.
    """
    if r < 0:
        raise ValueError("Radii cannot be negative")
    if type(r) not in [int, float]:
        raise TypeError("Radii can only be a positive real number.")
    return pi * (r ** 2)

