#!/usr/bin/python3

"""
This is the 1-write_file module.
it supplies one function:

"""


def write_file(filename="", text=""):
    """
    Function: write_file

    Args:
    filename - name of file
    text is the string you are writing to the file

    If the file exists, overwrite its contents.

    If it does not, create it automatically.

    Return: number of characters written
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        return file.write(text)
