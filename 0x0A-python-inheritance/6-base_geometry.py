#!/usr/bin/python3

"""
This is the 6-base_geometry module.
It supplies one class: BaseGeometry
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Methods:
        area
    """
    def area(self):
        """
        This is a public instance method, area.
        It raises an Exception with the message:
        area() is not implemented.
        """
        raise Exception("area() is not implemented")
