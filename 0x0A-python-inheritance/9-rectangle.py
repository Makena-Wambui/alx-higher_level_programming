#!/usr/bin/python3

"""
This is the 9-rectangle module
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
        area
        __str__

    Private Instance attributes:
        width
        height

    """
    def __init__(self, width, height):
        """
        __init__

        Python's constructor method.

        Called automatically each time the class is instantiated.

        Initializes private instance attibutes: width, height
        """
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def area(self):
        """
        Public instance method, area.

        Returns the area of each Rectangle object.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Magic method: __str__

        Returns an informal string representation of
        each Rectangle object.
        """
        return f"[{__class__.__name__}] {self.__width}/{self.__height}"
