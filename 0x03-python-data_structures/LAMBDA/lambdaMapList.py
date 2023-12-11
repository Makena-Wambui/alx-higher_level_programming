#!/usr/bin/python3
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
c = [16, 18, 9, 5]
d = [4, 9, 10]
m = list(map(lambda x, y, z: x + y + z, a, b, c))
print(m)
e = list(map(lambda s, t: s + t, a, d))
print(e)
f = list(map(lambda x, y: x ** 2 + y ** 3, a, d))
print(f)
