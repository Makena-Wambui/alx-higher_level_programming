#!/usr/bin/python3

"""
This is the 12-pascal_triangle module.
It supplies one function:
       pascal_triangle
"""


def pascal_triangle(n):
    """
    Function: pascal_triangle

    Args:
    -----
        n is an integer, which dictates how many rows of the Pascals
        triangle will be generated.
    Return:
        a list of lists of integers representing the Pascal's triangle of n
    """

    if n <= 0:
        return []
    tri = []

    for row_number in range(n):
        row = []
        for r in range(row_number + 1):
            coeff = 1
            if r > 0 and r < row_number:
                coeff = tri[row_number - 1][r - 1] + tri[row_number - 1][r]
            row.append(coeff)
        tri.append(row)

    return tri
