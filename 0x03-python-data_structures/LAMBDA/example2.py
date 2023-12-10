#!/usr/bin/python3
import sys  # so we can access the CLI arguments using sys.argv
from math import prod


def CommandLineArgs(arguments):
    # arguments is a list from sys.argv
    # convert each element into an integer

    arguments = [int(num) for num in arguments]
    total = prod(arguments)
    return total


if __name__ == '__main__':
    elements = sys.argv[1:]
    print(CommandLineArgs(elements))
