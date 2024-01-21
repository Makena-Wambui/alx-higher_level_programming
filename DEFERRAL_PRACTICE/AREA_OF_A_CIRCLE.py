#!/usr/bin/python3
from math import pi
"""This is the AREA_OF_A_CIRCLE module.
This module has one function area which computes the
area of a circle.
>>> Area(2)
12.566370614359172
"""


def Area(r):
    """This Area function returns the area of a circle of radius r.
    j is the square root of -1 in Python.
    >>> radii = [2, 2.5, 0, -3, 2 + 5j, True, "radius"]
    >>> message = "Area of circle with radius r, {} is {}."
    >>> for r in radii:
    ...     A = Area(r)
    ...     print(message.format(r, A))
    Area of circle with radius r, 2 is 12.566370614359172.
    Area of circle with radius r, 2.5 is 19.634954084936208.
    Area of circle with radius r, 0 is 0.0.
    Area of circle with radius r, -3 is 28.274333882308138.
    Area of circle with radius r, 2 + 5j is (-65.97344572538566+62.83185307179586j).
    Area of circle with radius r, True is 3.141592653589793.
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    """
    return pi * (r ** 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
