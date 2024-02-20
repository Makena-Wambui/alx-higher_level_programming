#!/usr/bin/python3

"""
This is the 2-append_write module.
It supplies one function:
    append_write
"""


def append_write(filename="", text=""):
    """
    Function: append_write

    Args
    ----
        filename: name of file
        text: string we are appending

    Return: No of characters added.

    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
