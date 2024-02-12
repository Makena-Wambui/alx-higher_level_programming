#!/usr/bin/python3

"""
This is the 10-square module.
It supplies one class: Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This is the class: Square
    It is derived from the Rectangle class.
    Therefore, it is a grendchild of BaseGeometry class.
    Methods:
        init
        area
        __str__

    """
    def __init__(self, size):
        """Python's constructor method.
        Each Square object is initialized with private attribute, size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
