#!/usr/bin/python3
"""This module contains the fefinition of the class Square."""


class Square:
    """This is the definition of the class Square.
    Each instance of the Square is initialized with
    the private attributes:
    size which is assigned the value of the size parameter
    position which is assigned the value of the position
    parameter."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """This property retrieves the value of the size
        attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter sets the size attibute to the value provided as an
        argument.
        We check if value is an integer using isinstance
        and raise an exception if it is not.
        We check if value is not negative.
        If it is, we raise an exception.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """This property retrieves the value of the
        position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """This setter sets the value of the position attribute to
        value.
        This value must be a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """This method returns the area of the Square object."""
        return (self.__size ** 2)

    def my_print(self):
        """This method prints the square as a pattern of '#'.
        The position tuple is used to indicate how many
        spaces should be left above the square and infront of each row of #s.
        If position is (2, 1):
        then there should be two spaces before each row of the square
        and 1 blank line before printing the square or above the square."""
        if self.__size == 0:
            print("")
            return

            """Print the blank lines as per position[1] above
            the square."""

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for a in range(self.__position[0]):
                print(' ', end='')
            for a in range(self.__size):
                print('#', end='')
            print()
