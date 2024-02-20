#!/usr/bin/python3
"""
This is the 8-class_to_json module.
It supplies one function:
    class_to_json(obj)

"""


def class_to_json(obj):
    """
    Function: class_to_json

    Args: obj

    This function takes obj,
    which is an instance of a class,
    and returns a dictionary of its attributes.
    This dictionary only contains simple data
    structures that can be serialized to json.
    the __dict__ attribute of an object contains
    a dictionary mapping attribute names to their values.

    Attributes: instance variables and methods.
    """
    return obj.__dict__
