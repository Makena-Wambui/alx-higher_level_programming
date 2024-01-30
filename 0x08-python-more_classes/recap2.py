#!/usr/bin/python3

"""The Pythonic way to introduce the attributes of a class is to make them public.
Let us rewrite the class from recap1."""

class P:

    def __init__(self, x):
        self.x = x


if __name__ == "__main__":
    a = P(2)
    b = P(1)
    print(b.x)
    b.x = 2
    print(b.x)
    b.x = a.x + b.x
    print(b.x)
    b.x = -1
    print(b.x)
    b.x = 2000
    print(b.x)
