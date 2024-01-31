#!/usr/bin/python3
"""
This is the 7-rectangle module.
It supplies one class, Rectangle.
"""


class Rectangle:
    """
    Class: Rectangle.
    Every Rectangle object is initialized with width and height,
    whose default values are 0 and 0 respectively.

    Private Instance Attributes:
        height
        width

    Public class attributes:
        number_of_instances
        print_symbol

    Properties:
        width
        width
        height
        height
    Methods:
        area
        perimeter
        __str__
        __repr__
        __del__
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        The init method is a constructor method.
        It is automatically called each time an instance of a class
        is created.
        Private instance attributes:
            Width
            Height
        """
        self.height = height
        self.width = width

        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        This property retrieves the value of the private
        instance attribute width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This property setter modifies the value of the
        private instance attribute, width
        """
        # width must be an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # width must not be less than 0
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        This property retrieves the value of the
        private instance attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This property setter modifies the value of the
        private instance attribute, height
        to value.
        """
        # height must be an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # height must not be less than 0
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        This is a public instance method, area.
        It returns the rectangle area.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        This is a public instance method, perimeter.
        It returns the rectangle perimeter.
        if width or height is equal to 0,
        perimeter is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """
        THis is also an instance magic method,
        that will be called everytime i want to print
        an instance of the class Rectangle.
        This method is also called when str is applied to a
        Rectangle object
        The object will be printed with the character '#'
        if width or height is equal to 0,return an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)
            result += '\n'
        return result

    def __repr__(self):
        """
        This is the repr method.
        It returns a string that can be parsed by the Python
        Interpreter, and with eval,
        be able to recreate the given class instance.
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        This method is called every time del function
        is applied on a Rectangle object.
        It is a destructor method.
        Every time an instance is deleted, this method is called.
        """
        print('Bye rectangle...')
        type(self).number_of_instances -= 1
