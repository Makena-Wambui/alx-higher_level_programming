#!/usr/bin/python3
import functools
add = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(add)
