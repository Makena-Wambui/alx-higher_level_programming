#!/usr/bin/python3

"""
This is the 5-save_to_json_file module.
It supplies one function:
    save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function: save_to_json_file

    Args
    ----
        my_obj: this is the python object that
        will be converted into the corresponding json string.

        Then it is dumped into a file, filename,
        opened for writing.

    This function writes an Object to a text file,
    using a JSON representation.
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
