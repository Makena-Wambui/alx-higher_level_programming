#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    n = list(map(lambda sublist: list(map(lambda x: x ** 2, sublist)), matrix))
    return n
