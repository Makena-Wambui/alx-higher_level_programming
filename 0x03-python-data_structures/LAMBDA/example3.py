#!/usr/bin/python3
import sys


def addingArgs(List):
    List = [int(element) for element in List]
    sum = 0
    for element in List:
        sum = sum + element
    return sum


if __name__ == '__main__':
    numbers = sys.argv[1:]
    print(addingArgs(numbers))
