#!/usr/bin/python3
import math

"""This is the Factorials module.
This module provides one function, Factorial.
For example,
>>> Factorial(5)
120
"""


def Factorial(n):
    """The Factorial function calculates the factorial of a number n.
    n has to be a positive number.
    >>> Factorial(2)
    2
    >>> Factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    n can be a float but it has be to be an exact integer.
    >>> Factorial(5.0)
    120
    >>> Factorial(5.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be an exact integer

    n can also not be a huuuge number.
    >>> Factorial(1e100)
    Traceback (most recent call last)
        ...
    OverflowError: n too large
    """
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be an exact integer.")
    if n+1 == n:
        raise OverflowError("n too large")
    result = 1
    number = 2
    while number <= n:
        result = result * number
        number = number + 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
