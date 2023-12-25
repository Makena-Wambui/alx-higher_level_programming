#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This is the definition of the class Square.
    Each class instance is initialized with private attributes
    size and position.
    Methods:
        __init__
        area
        my_print
    Attributes:
        size
        position
    Properties:
        size
        position
    Property setters:
        size
        position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """This property setter sets the attribute size with the value
        passed as argument."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the value of the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """This property setter assigns value to the attribute position."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                    'position must be a tuple of 2 positive integer'
                    )

        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError(
                    "position must be a tuple of 2 positive integer"
                    )
        self.__position = value

    def area(self):
        """This method returns the area of the Square object."""
        return (self.__size ** 2)

    def my_print(self):
        """This method pronts the Square object to stdout
        using '#'"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for row in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
            print()

    def __str__(self):
        """This special method prints an instance of this class.
        It has the same behavior as the my+print method."""
        a = ""
        if self.__size == 0:
            a += '\n'
        else:
            for i in range(self.__position[1]):
                a += '\n'
            for i in range(self.__size):
                a += " " * self.__position[0] + '#' * self.__size + '\n'
        return a.rstrip()
