#!/usr/bin/python3

# lets design a class in a javaesque way with getters and setters
# to encapsulate the private attribute self.__x
"""
lEts include changes in the setter method.
if x is less than 0, then set x to 0.
if x is greater than 1000, set x to 1000.
"""

class P:

    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


if __name__ == "__main__":
    a = P(10)
    b = P(20)
    print(b.get_x())
    b.set_x(5)
    print(b.get_x())
    """The following expression is ugly.
    It would be easier to write if the attribute was public.
    Refer to recap2 to see example of writing this class
    in a Pythonic way.
    """
    b.set_x(a.get_x() + b.get_x())
    print(b.get_x())
    c = P(1001)
    print(c.get_x())
    c.set_x(-1)
    print(c.get_x())

