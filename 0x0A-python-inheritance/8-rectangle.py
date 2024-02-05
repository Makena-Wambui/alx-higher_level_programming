#!/usr/bin/python3

"""
This is the 8-rectangle module.
It supplies two classes, Rectangle
and BaseGeometry.
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


class Rectangle(BaseGeometry):
    """
    This is class: Rectangle
    It is a sub class of class Base Geometry.
    Methods:
        __init__

    Attributes:
        width
        height

    """
    def __init__(self, width, height):
        """
        This is Python's constructor method.
        It is automatically called every time class instantiation occurs.
        It initializes each object variable with the
        attributes, width and height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
