#!/usr/bin/python3

"""
This is the 11-square module.

It supplies one class: Square.

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class: Square

    Inherits from parent: Rectangle.

    Methods:
        __init__
        area
        __str__
    Private instance attribute: size
    """

    def __init__(self, size):
        """
        Magic method: __init__

        Python's constructor method.

        Called automatically each time the class is instantiated.

        Initializes private instance attibute: size
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Public Instance Method: area

        Returns the area of a Square object

        """
        return self.__size ** 2

    def __str__(self):
        """
        Magic method: __str__

        Returns an informal string representation of a
        Square object.
        """
        return f"[{__class__.__name__}] {self.__size}/{self.__size}"
