#!/usr/bin/python3

"""
This is the 4-from_json_string module.
It supplies one function:
    from_json_string
"""
import json


def from_json_string(my_str):
    """
    Function: from_json_string

    Args:
    -----
        my_str: the json string

    This function returns an object (Python data structure)
    represented by a JSON string.
    """
    return (json.loads(my_str))
