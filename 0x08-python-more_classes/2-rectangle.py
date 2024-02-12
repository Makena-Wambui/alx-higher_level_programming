#!/usr/bin/python3

"""
This is the 2-rectangle module.
It supplies one class: Rectangle.
"""


class Rectangle:
    """
    This is the class Rectangle.

    Methods:
        __init__
        area

    Attributes:
        width
        height

    Properties:
        width
        height
    Property setters:
        width.setter
        height.setter

    """
    def __init__(self, width=0, height=0):
        """
        This is the Constructor method.
        It is called each time the class is instantiated.
        Each Rectangle object has attributes, width and height,
        whose values are initialized to the values of the parameters,
        width and height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property width that retrieves the value of the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Propery setter width to set the value of the
        attribute width to value.
        width must be an integer
        width should not be less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property height that retrieves the value of the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Propery setter height to set the value of the
        attribute height to value.
        height must be an integer
        height should not be less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This is a public instance method, area.
        It returns the area of a Rectangle object.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        This is a public instance method, perimeter.
        It returns the perimeter of a Rectangle object.
        if width or height is equal to 0, perimeter is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2
