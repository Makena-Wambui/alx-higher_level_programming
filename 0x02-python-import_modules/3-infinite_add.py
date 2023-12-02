#!/usr/bin/python3
import sys


def addArguments():
    sum = 0
    arguments = sys.argv
    for arg in arguments[1:]:
        sum = sum + int(arg)
    return sum


if __name__ == '__main__':
    print(addArguments())
