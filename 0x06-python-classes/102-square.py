#!/usr/bin/python3
"""This module contains the definition of
the class Square."""


class Square:
    """The init special method initializes every instance of the Square
    with a private attribute size.
    Methods:
        __init__
        area
        __equal__
        __not_equal__
        __greater__
        __greater_or_equal__
        __less__
        __less_or_equal__
    Attributes:
        size
    Propeties:
        size
    Property setter:
        size
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """This property retrieves the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter sets the value of the size attribute to value.
        Value must be a float or integer and greater than
        or equal to 0."""
        if (not isinstance(value, int) or not isinstance(value, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the area of the Square object."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Checks whether the areas of the two objects are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks whether the areas are not equal."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if area is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks whether area is greater than or equal to the other."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks whether the area is less than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks whether the area is less than or equal than the other."""
        return self.area() <= other.area()
