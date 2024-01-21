#!/usr/bin/python3
"""This SQUARES module provides one function called Square.
For example,
>>> Square(2)
4
"""


def Square(n):
    """This function returns the Square of a number n.
    >>> Square(3)
    9
    >>> Square(-4)
    16
    """
    return (n * n)


# use the __test__attribute to build or define a dictionary of tests.
__test__ = {
        "Square_zero": """
        >>> Square(0)
        0
        """,
        "Square_nine": """
        >>> Square(9)
        81
        """,
        "Square_negative_five": """
        >>> Square(-5)
        25
        """
}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
