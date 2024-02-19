#!/usr/bin/python3

"""
This is the 8-rectangle module
It supplies one class:
    Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class: Rectangle

    Inherits from BaseGeometry

    Methods:
        __init__

    Private Instance attributes:
        width
        height

    """
    def __init__(self, width, height):
        """
        __init__

        Python's constructor method.

        Called automatically each time the class is instantiated.

        Initializes instance attibutes: width, height
        """
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
