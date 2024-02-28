#!/usr/bin/python3

"""
This module contains tests for the Square Class.
"""

import sys
from io import StringIO
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestIsSubClass(unittest.TestCase):
    """
    Class: TestIsSubClass

    Lets test if Square is a subclass of Rectangle
    and Base.
    """

    def test_rectangle(self):
        """
        Test if Rectangle is the parent class of Square.
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_base(self):
        """
        Test if Basee is the parent class of Square.
        """
        self.assertTrue(issubclass(Square, Rectangle))


class TestIsInstance(unittest.TestCase):
    """
    Class: TestIsInstance.

    Lets test if Square object is an instance of Rectangle,
    Base and Square.
    """

    def test_isinstance(self):
        """
        Test if Square instance is an instance of Square.
        """
        self.assertTrue(isinstance(Square(3), Square))

        self.assertTrue(isinstance(Square(3), Rectangle))

        self.assertTrue(isinstance(Square(3), Base))

    def test_type(self):
        """
        Test if a Square object is exactly an instance of
        which class.
        """

        square_1 = Square(3)

        self.assertTrue(type(square_1) is Square)

        self.assertFalse(type(square_1) is Rectangle)

        self.assertFalse(type(square_1) is Base)


class TestInstantiation(unittest.TestCase):
    """
    Class: TestInstantiation

    Lets test various ways of instantiating a Square object.

    """

    def test_instantiation(self):
        """
        Test various ways of instantiating a Square object.
        """

        with self.assertRaises(TypeError):
            Square()

        square = Square(1)
        square_str = "[Square] ({}) 0/0 - 1".format(square.id)
        self.assertEqual(square_str, square.__str__())

        square1 = Square(2, 1)
        square1_str = "[Square] ({}) 1/0 - 2".format(square1.id)
        self.assertEqual(square1_str, square1.__str__())

        square2 = Square(2, 1, 1)
        square2_str = "[Square] ({}) 1/1 - 2".format(square2.id)
        self.assertEqual(square2_str, square2.__str__())

        square3 = Square(2, 1, 1, 89)
        square3_str = "[Square] (89) 1/1 - 2"
        self.assertEqual(square3_str, square3.__str__())

        with self.assertRaises(TypeError):
            Square(2, 1, 1, 89, 100)

        with self.assertRaises(NameError):
            square4.Square(2, 1, 1, 89)

    def test_bad_input(self):
        """
        Test invalid input.
        """

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "1")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "1")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 1, -1)


class TestStr(unittest.TestCase):
    """
    Class: TestStr

    Lets test the str method of class Square.
    """

    def test_str(self):
        """
        Tests for the str method of class Square.
        """

        square = Square(1)
        sq_str = "[Square] ({}) 0/0 - 1".format(square.id)
        self.assertEqual(sq_str, str(square))

        square2 = Square(1, 2)
        sq2_str = "[Square] ({}) 2/0 - 1".format(square2.id)
        self.assertEqual(sq2_str, str(square2))

        square3 = Square(1, 2, 1)
        sq3_str = "[Square] ({}) 2/1 - 1".format(square3.id)
        self.assertEqual(sq3_str, str(square3))

        square4 = Square(1, 2, 1, 89)
        sq4_str = "[Square] ({}) 2/1 - 1".format(square4.id)
        self.assertEqual(sq4_str, str(square4))

    def test_print(self):
        """
        Test if a call to print uses the str method.
        """
        string_capture = StringIO()
        sys.stdout = string_capture

        square = Square(1)
        print(square)
        string_capture = string_capture.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(string_capture, square.__str__())
