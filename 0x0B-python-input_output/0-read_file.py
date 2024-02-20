#!/usr/bin/python3

"""
This is the 0-read_file module.
It supplies one function:
    read_file

"""


def read_file(filename=""):
    """
    Function: read_file

    It reads a file and prints it to stdout.

    Args: filename
    """
    with open(filename, encoding='utf-8') as file:
        f = file.read()
        print(f)
