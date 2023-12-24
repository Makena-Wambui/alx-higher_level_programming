#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This is the definition of the class Square.
    Each instance of this class is initialized with a default size 0.
    The private instance attribute is assigned the value of the size parameter.
    We include a check to ensure size is an integer,
    and raise an exception if it is not.
    We check if size is less than 0,
    and raise an exception if it is.

    Methods:
        __init__

    Attributes:
        self.__size

    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
