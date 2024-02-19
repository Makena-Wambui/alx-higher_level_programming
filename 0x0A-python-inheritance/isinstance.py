#!/usr/bin/python3
"""
isinstance is used to check an instance's type
"""
a = 1
b = False
print(isinstance(a, int))
print(isinstance(b, bool))
print(isinstance(b, int))
print(a.__class__)
print(b.__class__.__name__)
