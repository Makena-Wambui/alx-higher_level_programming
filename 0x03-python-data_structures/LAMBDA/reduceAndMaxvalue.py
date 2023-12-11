#!/usr/bin/python3
from functools import reduce
# demonstrate use of reduce to find the maximum value of a list of numerical values
maximo = lambda x, y: x if (x > y) else y
a = reduce(maximo, [100, 3, 19, 1000,35])
print(a)
