#!/usr/bin/python3

"""
Python program to demonstrate error that occurs when
you forget to invoke the init of the parent class.
"""
class A(object):

    def __init__(self, name, location):
        self.name = name
        self.location = location


class B(A):
    def __init__(self, role):
        self.role = role


if __name__ == "__main__":
    a = B("nurse")
    print(a.name, a.location)
