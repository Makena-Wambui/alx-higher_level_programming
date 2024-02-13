#!/usr/bin/python3
"""This is the matrix_multiplied module"""


def matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for element in m_a:
        if not isinstance(element, list):
            raise TypeError("m_a must be a list of lists")

    for element in m_b:
        if not isinstance(element, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if not isinstance(elem, int) and type(elem) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if not isinstance(elem, int) and type(elem) is not float:
                raise TypeError("m_b should contain only integers or floats")

    # use this loop to loop through each row in the matrix
    # and compare the length of each row to the lenght of the first row.
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    # if number of columns in m_a are not equal to number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # empty matrix to store the result.
    m_result = []

    # Now we loop through the rows of m_a and the columns of m_b
    for i in range(len(m_a)):
        # append an empty row to m_result
        m_result.append([])
        for j in range(len(m_b[0])):
            m_result[i].append(0)
            for k in range(len(m_a[0])):
                m_result[i][j] += m_a[i][k] * m_b[k][j]

    return m_result
