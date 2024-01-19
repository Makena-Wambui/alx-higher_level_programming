#!/usr/bin/python3
"""This is the addition module.
This module supplies one function, adding function.For example,
>>> adding(2, 3)
5
"""


def adding(a, b):
    """This function returns the sum of two numbers.
    >>> adding(1, -1)
    0
    >>> adding(10,100)
    110
    >>> adding(1000, 1000)
    2000
    """
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
