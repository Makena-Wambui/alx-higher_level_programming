#!/usr/bin/python3
"""This is the 101-lazy_matrix_mul module.
Supplies the lazy_matrix_mul function."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices by using the module NumPy
    """
    return np.matmul(m_a, m_b)
