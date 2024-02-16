#!/usr/bin/python3
"""This is the 2-matrix_divided module.
It supplies one function: the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix with a number, div."""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    # each row must be of the same size:
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # all elements of each row must be an integer or float
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
    # div must be an integer or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # div can not be zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # create a new matrix
    new = []
    # for each row create a new row.
    # loop over each element in each row
    for row in matrix:
        new_row = []
        for i in row:
            # divide by div and round to two dps
            result = round(i / div, 2)
            # append result to new_row
            new_row.append(result)
        # append new rows to new matrix
        new.append(new_row)
    return new
