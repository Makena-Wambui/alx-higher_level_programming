#!/usr/bin/python3

"""
This is the 101-add_attribute module.
It supplies one function:
    add_attribute
"""


def add_attribute(obj, attribute_name, attribute_value):
    """
    Function: add_attribute

    Arguments:
        obj is the object we want to add the attribute into.
        attribute_name is the name of the attribute we want to add
        attribute_value is the value of that attribute.

    Hasattr checks whether the object has that attribute
    with the same name,
    in its __dict__attribute.
    If it does not, we can not add it so
    a TypeError exception is raised

    Setattr sets the attribute and its value if it is present.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute_name, attribute_value)
