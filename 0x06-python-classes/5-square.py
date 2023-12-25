#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """Every instance is initialized with a private instance attribute size
    that is assigned the value of the parameter size.

    Methods:
        __init__
        area
        my_print
    Attributes:
        size
    Property:
        size
    Setter:
        size
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """The property size returns the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """The setter size updates or modifies the value of the attribute size
        with the value provided as an argument.
        It performs ceratin checks.
        Check 1 is for whether that value is an integer.
        If not, a TypeEerror exception is raised.
        Check 2 is for whether that value is less than 0.
        If it is, a ValueEerror execption is raised."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This public instance method returns the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """This public instance method prints to stdout
        the pattern of the square depending on its size,
        using the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
