#!/usr/bin/python3

"""
This is the 6-load_from_json_file module.
It supplies one function:
    load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Function: load_from_json_file

    Args: filename

    This is a function that creates an Object
    from a “JSON file”
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        a = json.load(file)
        return a
