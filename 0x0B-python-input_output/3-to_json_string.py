#!/usr/bin/python3
"""
This is the 3-to_json_string module.
It supplies one function:
    to_json_string
"""
import json


def to_json_string(my_obj):
    """
    Function: to_json_string

    Args: my_obj
        This is the object we are converting to a JSON string.

    This function returns the JSON representation of an object (string)
    """
    return (json.dumps(my_obj))
