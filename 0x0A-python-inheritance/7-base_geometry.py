#!/usr/bin/python3

"""
This is the 7-base_geometry module.
It supplies one class: BaseGeometry
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Methods:
        area
        integer_validator
    """
    def area(self):
        """
        This is a public instance method, area.
        It raises an Exception with the message:
        area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is a public instance method, integer_validator.
        It validates value.
        name is always a string.
        if value is not an integer:
        raise a TypeError exception,with the message
        <name> must be an integer.
        if value is less or equal to 0:
        raise a ValueError exception with the message
        <name> must be greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
