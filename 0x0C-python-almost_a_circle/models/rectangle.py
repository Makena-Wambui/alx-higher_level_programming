#!/usr/bin/python3
"""
This is the rectangle module.
It supplies one class:
    Rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """
    Class: Rectangle

    This is a subclass of Base

    Private instance attributes:
    __width
    __height
    __x
    __y

    Methods:
    __init__
    area
    display
    __str_
    update
    to_dictionary

    Static method:
    validator

    Getters:
    width
    height
    x
    y

    Setters:
    width
    height
    x
    y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The Class Constructor

        Called automatically each time the class is instantiated.

        Sets all private instance attributes to the values of their
        corresponding arguments.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Public getter for the width attribute.
        Retrieves the value of the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Public setter for the width attribute.

        Sets the value of the width attribute to val.
        """
        self.validator("width", val)
        self.__width = val

    @property
    def height(self):
        """
        Public getter for the height attribute.
        Retrieves the value of the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Public setter for the height attribute.

        Sets the value of the height attribute to val.
        """
        self.validator("height", val)
        self.__height = val

    @property
    def x(self):
        """
        Public getter for the x attribute.
        Retrieves the value of the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Public setter for the x attribute.

        Sets the value of the x attribute to val.
        """
        self.validator("x", val)
        self.__x = val

    @property
    def y(self):
        """
        Public getter for the y attribute.
        Retrieves the value of the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Public setter for the y attribute.

        Sets the value of the y attribute to val.
        """
        self.validator("y", val)
        self.__y = val

    @staticmethod
    def validator(attr, val):
        """
        Static Method:
        validator

        Adds validation of all setter methods and instantiation.
        """
        if type(val) is not int:
            raise TypeError(f"{attr} must be an integer")

        if attr in ["width", "height"]:
            if val <= 0:
                raise ValueError(f"{attr} must be > 0")
        if attr in ["x", "y"]:
            if val < 0:
                raise ValueError(f"{attr} must be >= 0")

    def area(self):
        """
        Public instance method: area

        Returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        Public instance method: display
        Prints in stdout the Rectangle instance with the character #
        """

        # first print empty lines to accpmodate offset 'y'
        for i in range(self.y):
            print()

        for row in range(self.height):
            # then print empty spaces to accomodate offset 'x'
            # before printing '#'
            for j in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """
        Magic method: __str__

        Returns an informal string representation of our Rectangle objects.

        """
        return (f"[{__class__.__name__}] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        Public instance method: update
        Args: *args, **kwargs

        Assigns a key, value argument to each attribute.
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        Public instance method: to_dictionary

        Returns the dictionary representation of a Rectangle object.

        """
        return {'x': getattr(self, 'x'), 'y': getattr(self, 'y'),
                'id': getattr(self, 'id'), 'height': getattr(self, 'height'),
                'width': getattr(self, 'width')}
