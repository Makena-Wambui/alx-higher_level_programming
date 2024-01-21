#!/usr/bin/python3
"""This is the backslash module which is trying to illustrate
a raw docstring example.
"""


def f(x):
    """this is my f function.
    Using backslashes here for doctest.
    r '''My name is Alicia and \'''
    i am 30 years old.
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
