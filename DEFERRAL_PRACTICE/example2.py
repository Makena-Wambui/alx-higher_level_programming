#!/usr/bin/python3
from math import floor

n = int(input("Enter the number: "))


def calculate_factorial():
    if n == 0 or n == 1:
        return 1
    if n < 0:
        raise ValueError("n must be positive.")
    if floor(n) != n:
        raise ValueError("n must be an exact integer.")

    result = 1
    for i in range(1, n+1):
        result *= i
    return result


if __name__ == '__main__':
    print("Factorial of {} is {}.".format(n, calculate_factorial()))
