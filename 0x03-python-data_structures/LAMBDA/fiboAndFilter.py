#!/usr/bin/python3
import sys


def Fibo(n):
    a, b = 0, 1
    fib = []
    while a < n:
        fib.append(a)
        a, b = b, a + b
    return fib


if __name__ == '__main__':
    fib = Fibo(int(sys.argv[1]))
    print(fib)
    evens = list(filter(lambda x: x % 2 == 0, fib))
    odds = list(filter(lambda x: x % 2 == 1, fib))
    print(evens)
    print(odds)
