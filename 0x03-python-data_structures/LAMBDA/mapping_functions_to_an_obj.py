#!/usr/bin/python3
from math import sin, cos, tan, pi


def Functions(x, funcs):
    List = []
    for f in funcs:
        List.append(f(x))
    return List


Fam = [sin, cos, tan]
print(Functions(pi, Fam))
