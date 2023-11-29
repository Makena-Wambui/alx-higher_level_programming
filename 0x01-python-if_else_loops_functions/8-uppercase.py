#!/usr/bin/python3
def uppercase(str):
    for c in str:
        capital = chr(ord(c) - 32) if 'a' <= c <= 'z' else c
        print("{:s}".format(capital), end="")
    print()
