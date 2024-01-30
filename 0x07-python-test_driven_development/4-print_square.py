#!/usr/bin/python3
"""This is the 4-print_square module.
It supplies one function, print_square.
"""


def print_square(size):
    """This function prints a square with '#' character
    of size, size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
