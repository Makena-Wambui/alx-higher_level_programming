#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = list(map(lambda sublist: list(map(lambda x: x ** 2, sublist)), matrix))
    return a
