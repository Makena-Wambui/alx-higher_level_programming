#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """Here lies the definition of the class Square.
    Each instance or object of this class shall be instantiated
    with the private attribute size whose value is assigned the value
    of the size parameter.

    Methods:
        __init__
        area

    Attributes:
        size

    Properties:
        size
    Setter:
        size
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """This is a property used to retrieve
        the value of the private attribute size."""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter is used to update the value of the siaze
        attribute. It also performs some conditional checks for
        that value to ensure it is an integer and that
        it is not less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This is a public instance method that
        returns the area of the square."""
        return (self.__size ** 2)
