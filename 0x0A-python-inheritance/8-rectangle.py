#!/usr/bin/python3

"""
This is the 8-rectangle module.
It supplies one class, Rectangle.
"""

module = __import__("7-base_geometry")

BaseGeometry = getattr(module, "BaseGeometry")


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
