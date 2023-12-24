#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """This is the definition of the class Square.
    The private insance attribute size is assigned the
    value of the size parameter passed when we
    create an instance of the class.
    We check if size is an integer using isinstance function.
    We raise a TypeError if it is not.
    We also check if size is less than 0.
    We raise a ValuError if it is.
    Methods:
        __init__
        area

    Attributes:
        self.__size"""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This method area returns the area of an object or
        an instance of the class Square.
        It squares the value of the size attribute."""
        return (self.__size ** 2)
