#!/usr/bin/python3
from math import sin, cos, tan, pi


def Functions(x, Funcs):
    return [F(x) for F in Funcs]


Funcs = (sin, cos, tan)
print(Functions(pi, Funcs))
