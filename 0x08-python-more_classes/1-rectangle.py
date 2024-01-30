#!/usr/bin/python3

"""This is the 1-rectangle module.
It supplies one class, Rectangle.
"""


class Rectangle:
    """Class: Rectangle.
    Every Rectangle object is initialized with width and height,
    whose default values are 0 and 0 respectively.

    Attributes:
        height
        width
    Properties:
        width
        width
        height
        height
    """
    def __init__(self, width=0, height=0):
        """The init method is a constructor method.
        It is automatically called each time an instance of a class
        is created.
        Private instance attributes:
            Width
            Height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """This property retrieves the value of the private
        instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """This property setter modifies the value of the
        private instance attribute, width
        to value.
        """
        # width must be an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # width must not be less than 0
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """This property retrieves the value of the
        private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This property setter modifies the value of the
        private instance attribute, height
        to value.
        """
        # height must be an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # height must not be less than 0
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
