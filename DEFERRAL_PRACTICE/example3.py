#!/usr/bin/python3
"""
We can also use the built in function from math module."""
from math import factorial

number = int(input().strip())
print("The factorial of {} is {}".format(number, factorial(number)))
