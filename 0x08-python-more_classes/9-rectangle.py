#!/usr/bin/python3

"""
This is the 9-rectangle module.
It supplies one class: Rectangle.
"""


class Rectangle:
    """
    This is the class Rectangle.

    Methods:
        __init__
        area
        perimeter
        __str__
        __repr__
        bigger_or_equal(rect_1, rect_2)
        square(cls, size=0)

    Attributes:
        width
        height
    Public class Attributes:
        number_of_instances
        print_symbol

    Properties:
        width
        height
    Property setters:
        width.setter
        height.setter

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        This is the Constructor method.
        It is called each time the class is instantiated.
        Each Rectangle object has attributes, width and height,
        whose values are initialized to the values of the parameters,
        width and height.
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Property width that retrieves the value of the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Propery setter width to set the value of the
        attribute width to value.
        width must be an integer
        width should not be less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property height that retrieves the value of the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Propery setter height to set the value of the
        attribute height to value.
        height must be an integer
        height should not be less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This is a public instance method, area.
        It returns the area of a Rectangle object.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        This is a public instance method, perimeter.
        It returns the perimeter of a Rectangle object.
        if width or height is equal to 0, perimeter is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        This is the magic method, __str__.
        It is called each time we want to print a Rectangle object.
        It returns an informal string representation of an object.
        It makes objects readable.
        We use str when we intend to generate output for the end
        user.
        It uses the '#' character to represent an object.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        objectstr = ''

        # outer loop represents rows, hence height
        # inner loop represents columns hence width

        for i in range(self.__height):
            for j in range(self.__width):
                objectstr += str(self.print_symbol)
            # print a new line after each row
            objectstr += '\n'
        return objectstr[:-1]
        # sliced to remove the additional line

    def __repr__(self):
        """
        repr returns the canonocal string representation
        of an object.
        We can use the return value of repr together wit eval to
        recreate our Rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        This is the magic method del.
        Each time an instance of a class is deleted, this method is called.
        In this program, Bye Rectangle is printed
        each time a Rectangle object is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This is a static method.
        Static methods do not need a reference to self
        or cls.
        They do not affect the state of an object
        or class.
        But they can take other arbitrary parameters.
        It returns the biggest rectangle based on the area.
        """

        # rect_1 must be an instance of Rectangle
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        # rect_2 must be an instance of Rectangle
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        This is a class method.
        Class methods affect the state of the class,
        but they can not directly affect the state of an object.
        It returns a new Rectangle instance,
        with  width == height == size.
        """
        return cls(size, size)
