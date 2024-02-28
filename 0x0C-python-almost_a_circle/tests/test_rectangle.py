#!/usr/bin/python3

"""
This module contains tests for the Rectangle class.

"""
import unittest
import sys
import os
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class: TestRectangle.

    A subclass of TestCase class from unittest module.

    Contains methods that test the Rectangle class:
        test_issubclass
        test_rectangle_instantiation
        test_id
        test_if_equal
        test_access_to_private_attrs
        test_setters
        test_area
        test_getters
        test_validator
    """

    def test_issubclass(self):
        """
        Tests whether Rectangle is a subclass of Base
        """
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(issubclass(Rectangle, object))

    def test_rectangle_instantiation(self):
        """
        Test overall Rectangle Instantiation.
        """
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(1)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, 0, 4, 5)

    def test_id(self):
        """
        Tests the id attribute.
        """
        a = Rectangle(1, 2)
        b = Rectangle(3, 4)
        self.assertEqual(a.id, b.id - 1)

        r1 = Rectangle(2, 3, 4)
        r2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r1.id, r2.id - 1)

        r3 = Rectangle(2, 3, 4, 5, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(4, 5)
        self.assertEqual(r2.id, r4.id - 1)

    def test_if_equal(self):
        """
        Test if two Rectangle objects with same height
        and width are equal or same object.
        """
        r1 = Rectangle(3, 4)
        r2 = Rectangle(3, 4)
        self.assertNotEqual(r1, r2)
        self.assertFalse(r1 is r2)

    def test_access_to_private_attrs(self):
        """
        Test if access to private instance attributes is possible.
        """
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        with self.assertRaises(AttributeError):
            r1.__width
            r1.__height

        r2 = Rectangle(2, 6, 2, 1)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)
        with self.assertRaises(AttributeError):
            r1.__x
            r1.__y

    def test_getters(self):
        """
        Test the getters for each attribute.
        """
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

        r = Rectangle(3, 4, 1, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_setters(self):
        """
        Test the setters for each attribute.
        """
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.width, 3)
        r1.width = 4
        self.assertEqual(r1.width, 4)

        self.assertEqual(r1.height, 4)
        r1.height = 10
        self.assertEqual(r1.height, 10)

        self.assertEqual(r1.x, 0)
        r1.x = 2
        self.assertEqual(r1.x, 2)

        self.assertEqual(r1.y, 0)
        r1.y = 3
        self.assertEqual(r1.y, 3)

    def test_validator(self):
        """
        Test if validator method is successfully called by
        the setter each time
        we try to modify an attribute.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("Holberton", 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle([1, 2], 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({1, 2}, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({'a': 1, 'b': 2}, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(2.1, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle((3, 4), 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(frozenset([1, 2]), 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(b"school", 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(bytearray(b"school"), 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(None, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(complex(1, 10), 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(False, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(float('inf'), 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(float('-inf'), 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(float('nan'), 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(-2, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, "school")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, [1, 2])

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, {3, 4})

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, {'a': 1, 'b': 2})

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, 3.14)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, (1, 2))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, frozenset([1, 2]))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, b"school")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, bytearray(b"school"))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, None)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, True)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, complex(1, 10))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, float('inf'))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, float('-inf'))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, float('nan'))

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(2, 0)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(2, -2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, "hi")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, [1, 2])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, {1, 2})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, {'a': 1, 'b': 2})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, (1, 2))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, 1.2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, frozenset([1, 2]))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, b"hi")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, bytearray(b"hi"))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, None)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, True)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, float('nan'))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, float('inf'))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, float('-inf'))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, complex(1, 10))

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(2, 3, -1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, "hi")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, [1, 2])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, {1, 2})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, {'a': 1, 'b': 2})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, 1.2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, (1, 2))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, frozenset([1, 2]))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 2, 1, b"school")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, bytearray(b"school"))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, True)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, complex(2, 5))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, float('inf'))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, float('-inf'))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 3, 2, float('nan'))

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(1, 3, 2, -2)

    def test_area(self):
        """
        Test the area method of class Rectangle.
        """
        r1 = Rectangle(3, 4)
        self.assertEqual(12, r1.area())

        with self.assertRaises(TypeError):
            r1.area(1)

        r2 = Rectangle(100000000, 9000000)
        self.assertEqual(900000000000000, r2.area())

        with self.assertRaises(TypeError):
            r1.area(1, 3)

        r2.width = 1
        self.assertEqual(9000000, r2.area())

        r1.height = 10
        self.assertEqual(30, r1.area())


class TestStr(unittest.TestCase):
    """
    Class: TestStr

    Supplies methods for testing the str method of class Rectangle.

    Methods: test_str
    """

    def test_str(self):
        """
        Tests the str method from class Rectangle.
        """
        r1 = Rectangle(2, 3)
        r1_str = "[Rectangle] ({}) 0/0 - 2/3".format(r1.id)
        self.assertEqual(str(r1), r1_str)

        r2 = Rectangle(3, 5, 1)
        r2_str = "[Rectangle] ({}) 1/0 - 3/5".format(r2.id)
        self.assertEqual(str(r2), r2_str)

        r3 = Rectangle(3, 4, 2, 1)
        r3_str = "[Rectangle] ({}) 2/1 - 3/4".format(r3.id)
        self.assertEqual(r3.__str__(), r3_str)

        r4 = Rectangle(3, 4, 5, 2, 6)
        r4_str = "[Rectangle] (6) 5/2 - 3/4"
        self.assertEqual(r4.__str__(), r4_str)

        r4.width = 2
        r4.height = 6
        r4.x = 3
        r4.y = 1
        r4.id = 10
        r4_str = "[Rectangle] (10) 3/1 - 2/6"
        self.assertEqual(str(r4), r4_str)

        # from io package import StringIO module
        # StringIO allows you to capture output
        # that would normally go to the console
        # and redirect it to a string variable
        # which we can use to compare with our expected output
        output = StringIO()
        sys.stdout = output
        print(r4)
        my_output = output.getvalue().strip()

        # make sure to reset stdout to default
        sys.stdout = sys.__stdout__
        self.assertEqual(my_output, "[Rectangle] (10) 3/1 - 2/6")

        with self.assertRaises(TypeError):
            r4.__str__(9)


class TestDisplay(unittest.TestCase):
    """
    Class: TestDisplay

    A subclass of unittest.TestCase

    Contains methods that test the display method.

    Methods:
        test_display_no_offset
        test_display_with_xi
        test_display_with_y
        test_display_both_offsets
        test_display_with_excess_parameters

    """

    def test_display_no_offset(self):
        """
        Tests the display method of class Rectangle.
        x = 0, y = 0
        """
        r4 = Rectangle(2, 3)

        output2 = StringIO()
        sys.stdout = output2
        r4.display()
        my_output2 = output2.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(my_output2, "##\n##\n##\n")

    def test_display_with_x(self):
        """
        Tests the display method of class Rectangle.
        x = 1
        y = 0
        """
        r = Rectangle(2, 3, 1)

        output_3 = StringIO()
        sys.stdout = output_3
        r.display()
        my_output3 = output_3.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(my_output3, " ##\n ##\n ##\n")

    def test_display_with_y(self):
        """
        Tests the display method of class Rectangle.
        x = 0
        y = 1
        """
        r = Rectangle(2, 3, 0, 1)

        output = StringIO()
        sys.stdout = output
        r.display()
        output = output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(output, "\n##\n##\n##\n")

    def test_display_both_offsets(self):
        """
        Tests the display method of class Rectangle.
        Both offsets present
        x = 1
        y = 2
        """
        r = Rectangle(2, 3, 1, 2)

        output = StringIO()
        sys.stdout = output
        r.display()
        output = output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(output, "\n\n ##\n ##\n ##\n")

    def test_display_with_excess_parameters(self):
        """
        Tests the display method of class Rectangle.
        display called with extra parameter.
        """
        r = Rectangle(2, 3, 1, 2)

        with self.assertRaises(TypeError):
            r.display(2)


class TestUpdateArgs(unittest.TestCase):
    """
    Class: TestUpdateMethod

    A subclass of unittest.TestCase

    Contains methods that test the args argument of update
    method.

    Methods:
        test_no_arguments
        test_one_argument
        test_two_arguments
        test_three_arguments
        test_four_arguments
        test_five_arguments
        test_more_than_five
        test_double_update
        test_none_id
        test_none_plus_more_args
        test_update_with_bad_width
        test_update_with_bad_height
        test_update_with_bad_x
        test_update_with_bad_y
        test_mixed_bad_input
    """

    def test_no_arguments(self):
        """
        Tests the update method of class Rectangle.
        No arguments passed to update.
        """

        r = Rectangle(2, 3)
        r.update()
        updated_r = "[Rectangle] ({}) 0/0 - 2/3".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_one_argument(self):
        """
        Tests the update method of class Rectangle.
        One argument passed to update.
        Expected to affect id.
        """
        r = Rectangle(2, 3)
        r.update(10)
        updated_r = "[Rectangle] ({}) 0/0 - 2/3".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_two_arguments(self):
        """
        Tests the update method of class Rectangle.
        Two arguments passed to update.
        Expected to affect id and width
        """
        r = Rectangle(2, 3)
        r.update(10, 3)
        updated_r = "[Rectangle] ({}) 0/0 - 3/3".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_three_arguments(self):
        """
        Tests the update method of class Rectangle.
        Three arguments passed to update.
        Expected to affect id, width, height
        """
        r = Rectangle(2, 3)
        r.update(10, 3, 6)
        updated_r = "[Rectangle] ({}) 0/0 - 3/6".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_four_arguments(self):
        """
        Tests the update method of class Rectangle.
        Four arguments passed to update.
        Expected to affect id, width, height, x
        """
        r = Rectangle(2, 3)
        r.update(10, 3, 6, 2)
        updated_r = "[Rectangle] ({}) 2/0 - 3/6".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_five_arguments(self):
        """
        Tests the update method of class Rectangle.
        Five arguments passed to update.
        Expected to affect id, width, height, x, y
        """
        r = Rectangle(2, 3)
        r.update(10, 3, 6, 2, 2)
        updated_r = "[Rectangle] ({}) 2/2 - 3/6".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_more_than_five(self):
        """
        Tests the update method of class Rectangle.
        More than Five arguments passed to update.
        Expected to affect id, width, height, x, y
        """
        r = Rectangle(2, 3)
        r.update(10, 3, 6, 2, 2, 4)
        updated_r = "[Rectangle] ({}) 2/2 - 3/6".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_double_update(self):
        """
        Tests the update method of class Rectangle.
        Calls update twice on an object.
        """
        r = Rectangle(2, 3)
        r.update(10, 3, 6, 2, 2)
        r.update(50, 10, 5, 4, 0)
        updated_r = "[Rectangle] ({}) 4/0 - 10/5".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_none_id(self):
        """
        Tests the update method of class Rectangle.
        Call update with id = None
        """
        r = Rectangle(2, 3)
        r.update(None)
        updated_r = "[Rectangle] ({}) 0/0 - 2/3".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_none_plus_more_args(self):
        """
        Tests the update method of class Rectangle.
        Call update with id = None and additional args
        """
        r = Rectangle(2, 3)
        r.update(None, 6, 8, 1, 3)
        updated_r = "[Rectangle] ({}) 1/3 - 6/8".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_update_with_bad_width(self):
        """
        Tests the update method of class Rectangle.
        Call update with invalid width.
        """
        r = Rectangle(2, 3)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "width", 8, 1, 3)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, [1, 2], 8, 1, 3)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, (1, 2), 8, 1, 3)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, 0, 8, 1, 3)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, -2, 8, 1, 3)

    def test_update_with_bad_height(self):
        """
        Tests the update method of class Rectangle.
        Call update with invalid height.
        """
        r = Rectangle(2, 3)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(100, 10, "hello")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(100, 10, [1, 2])

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(100, 10, (1, 2))

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(100, 10, 0)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(100, 10, -1)

    def test_update_with_bad_x(self):
        """
        Tests the update method of class Rectangle.
        Call update with invalid x.
        """
        r = Rectangle(2, 3)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(100, 10, 20, "hi")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(100, 10, 20, {1, 2})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(100, 10, 20, (1, 2))

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(100, 10, 20, -1)

    def test_update_with_bad_y(self):
        """
        Tests the update method of class Rectangle.
        Call update with invalid y.
        """
        r = Rectangle(2, 3)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(100, 10, 20, 1, "hi")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(100, 6, 12, 1, [1, 2])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(100, 6, 12, 1, (1, 2))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(100, 6, 12, 1, {1, 2})

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(100, 6, 12, 1, -1)

    def test_mixed_bad_input(self):
        """
        Tests the update method of class Rectangle.
        Calls update with various invalid input.
        """
        r = Rectangle(2, 3)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "hello", 6)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "hello", "hi")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "hello", "hi", -1, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, 1.5, "hi")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "hello", "hi", -1, (1, 2))

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "hello", 6, 0, 1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, 0, 6)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, -2, "hello", 1, 2)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, -5, 4, -1, -1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 2, "hello")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 2, 5.6, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 2, "hello", -1, 3)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 2, (1, 2), -1, -1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(10, 2, 0, -1, -1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(10, 2, 0, 1, 1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(10, 4, -1, -1, -2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(10, 4, -2, 1, 2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(10, 4, 5, "hi", "hello")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(10, 4, 5, "hi", 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(10, 4, 5, (1, 2), 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(10, 4, 5, {"a": 1, "b": 2}, (1, 2))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(10, 4, 5, 1.2, 1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(10, 4, 5, -1, 1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(10, 4, 5, -1, -1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(10, 4, 6, 0, 1.5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(10, 4, 6, 0, [1, 2])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(10, 4, 6, 0, "hi")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(10, 4, 6, 0, (1, 2))

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(10, 4, 6, 0, -1)


class TestKwargs(unittest.TestCase):
    """
    Class: TestKwargs

    A subclass of unittest.TestCase

    Contains methods that test the keyword arguments passed
    to the update method of class Rectangle.

    Methods:
        test_none_id
        test_reg_id
        test_width_kwargs
        test_more_kwargs
        test_more
        test_more_plus
        test_none_id_plus
        test_kwargs_twice
        test_args_skipped
        test_update_with_bad_keys
        test_update_not_all_bad_keys
        test_bad_width
        test_bad_height
        test_bad_x
        test_bad_y


    """

    def test_no_args(self):
        """
        This method tests for 0 args passed to update.
        """
        r = Rectangle(3, 4)
        r.update()
        updated_r = "[Rectangle] ({}) 0/0 - 3/4".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_none_id(self):
        """
        Tests the kwargs argument of the update method.
        id = None.
        """

        r = Rectangle(3, 4)
        r.update(id=None)
        updated_r = "[Rectangle] (None) 0/0 - 3/4"
        self.assertEqual(updated_r, r.__str__())

    def test_none_id_plus(self):
        """
        Tests the kwargs argument of the update method.
        id = None
        width = 5
        x= 2
        """
        r = Rectangle(3, 4)
        r.update(width=5, x=2, id=None)
        updated_r = "[Rectangle] (None) 2/0 - 5/4"
        self.assertEqual(updated_r, r.__str__())

    def test_reg_id(self):
        """
        Tests the kwargs argument of the update method.
        id = 100
        """
        r = Rectangle(3, 4)
        r.update(id=100)
        updated_r = "[Rectangle] (100) 0/0 - 3/4"
        self.assertEqual(updated_r, r.__str__())

    def test_width_kwargs(self):
        """
        Tests the kwargs argument of the update method.
        width=6
        id = 20
        """
        r = Rectangle(3, 4)
        r.update(id=20, width=6)
        updated_r = "[Rectangle] (20) 0/0 - 6/4"
        self.assertEqual(updated_r, r.__str__())

    def test_more_kwargs(self):
        """
        Tests the kwargs argument of the update method.
        width= 2
        height=8
        id=None
        """
        r = Rectangle(3, 4)
        r.update(id=None, width=2, height=8)
        updated_r = "[Rectangle] (None) 0/0 - 2/8"
        self.assertEqual(updated_r, r.__str__())

    def test_more(self):
        """
        Tests the kwargs argument of the update method.
        id=80
        width = 10
        height = 20
        x = 3
        """
        r = Rectangle(3, 4)
        r.update(id=80, width=10, height=20, x=3)
        updated_r = "[Rectangle] (80) 3/0 - 10/20"
        self.assertEqual(updated_r, r.__str__())

    def test_more_plus(self):
        """
        Tests the kwargs argument of the update method.
        id = 80
        width = 10
        height = 20
        x= 3
        y = 2
        """
        r = Rectangle(3, 4)
        r.update(id=80, width=10, height=20, x=3, y=2)
        updated_r = "[Rectangle] (80) 3/2 - 10/20"
        self.assertEqual(updated_r, r.__str__())

    def test_kwargs_twice(self):
        """
        Tests the kwargs argument of the update method.
        We call update twice on an object and each time pass
        different kwargs values.
        """
        r = Rectangle(3, 4)
        r.update(id=None, width=9, y=2)
        r.update(id=100, height=5, width=3, x=1)
        updated_r = "[Rectangle] (100) 1/2 - 3/5"
        self.assertEqual(updated_r, r.__str__())

    def test_args_skipped(self):
        """
        Tests the kwargs argument of the update method.
        If args are present, then kwargs should be skipped.
        """
        r = Rectangle(3, 4)
        args = (100, 6, 8, 2)
        kwargs = {"y": 2, "height": 15, "id": None}
        r.update(*args, **kwargs)
        updated_r = "[Rectangle] (100) 2/0 - 6/8"
        self.assertEqual(updated_r, r.__str__())

    def test_update_with_bad_keys(self):
        """
        Tests the kwargs argument of the update method.
        The dictionary, kwargs has key,value pairs that
        our Rectangle objects dont have.
        Therefore, update should fail.
        """
        r = Rectangle(5, 10)
        kwargs = {"name": "alicia", "age": 50}
        r.update(**kwargs)
        updated_r = "[Rectangle] ({}) 0/0 - 5/10".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_update_not_all_bad_keys(self):
        """
        Tests the kwargs argument of the update method.
        The dictionary, kwargs has some key,value pairs that
        our Rectangle objects dont have.
        """
        r = Rectangle(5, 10)
        kwargs = {"y": 2, "name": "alicia", "width": 4, "age": 50}
        r.update(**kwargs)
        updated_r = "[Rectangle] ({}) 0/2 - 4/10".format(r.id)
        self.assertEqual(updated_r, r.__str__())

    def test_bad_width(self):
        """
        Tests the kwargs argument of the update method.
        Checking if Exception is successfully raised if
        invalid width is passed.
        """
        r = Rectangle(3, 4)
        kwargs = {"height": 7, "width": "hello"}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(**kwargs)

        kwargs = {"height": 7, "width": 3.14}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(**kwargs)

        kwargs = {"height": 7, "width": [1, 2]}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(**kwargs)

        kwargs = {"height": 7, "width": 0}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(**kwargs)

        kwargs = {"height": 7, "width": -5}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(**kwargs)

    def test_bad_height(self):
        """
        Tests the kwargs argument of the update method.
        Checking if Exception is successfully raised if
        invalid height is passed.
        """
        r = Rectangle(5, 8)
        kwargs = {"width": 6, "height": "mom"}
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(**kwargs)

        kwargs = {"width": 6, "height": 1.5}
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(**kwargs)

        kwargs = {"height": [1, 2], "width": 1.5}
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(**kwargs)

        kwargs = {"height": 0, "width": 1}
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(**kwargs)

        kwargs = {"height": -1, "width": 1}
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(**kwargs)

    def test_bad_x(self):
        """
        Tests the kwargs argument of the update method.
        Checking if Exception is successfully raised if
        invalid x is passed.
        """
        r = Rectangle(5, 10)
        kwargs = {"x": 1.2, "width": -1, "height": 5}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(**kwargs)

        kwargs = {"x": [1, 2], "width": 1, "height": 5}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(**kwargs)

        kwargs = {"x": "jake", "width": 1, "height": 5}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(**kwargs)

        kwargs = {"x": -1, "width": 6}
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(**kwargs)

    def test_bad_y(self):
        """
        Tests the kwargs argument of the update method.
        Checking if Exception is successfully raised if
        invalid x is passed.
        """
        r = Rectangle(5, 10)
        kwargs = {"y": "jake", "width": "son", "x": (1, 2)}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(**kwargs)

        kwargs = {"y": 1.5, "x": 5, "width": 6.7}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(**kwargs)

        kwargs = {"y": [1, 2], "x": 5, "width": 6}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(**kwargs)

        kwargs = {"y": -2, "x": -5, "width": 6}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(**kwargs)


class TestDictionary(unittest.TestCase):
    """
    Class: TestDictionary

    A subclass Of unittest.TestCase.

    Contains methods that test the to_dictionary method
    from class Rectangle.

    Methods:
        test_1
        test_different_objects
        test_excess_args
    """

    def test_1(self):
        """
        Tests if call to to_dictionary produces a dictionary
        with expected order of attributes.
        """

        r = Rectangle(3, 4, 1, 2, 12)
        d = {"x": 1, "y": 2, "id": 12, "height": 4, "width": 3}
        self.assertDictEqual(d, r.to_dictionary())

    def test_different_objects(self):
        """
        Pass the output produced by call to to_dictionary
        as argument to update method.

        """
        r = Rectangle(3, 4, 1, 2, 12)
        r1 = Rectangle(2, 6, 2, 1, 4)
        r_dict = r.to_dictionary()
        self.assertNotEqual(r_dict, r1.update(**r_dict))

    def test_excess_args(self):
        """
        Tests if Exception is raised when excess arguments are passed
        to to_dictionary
        """
        r = Rectangle(3, 4, 1, 2, 12)
        with self.assertRaises(TypeError):
            r.to_dictionary(2)

        with self.assertRaises(TypeError):
            r.to_dictionary(2, 1)


class TestJson(unittest.TestCase):
    """
    Class: TestJson

    Contains methods that test json methods inherited from superclass Base

    Method: test_to_json_string
            test_from_json_string

    """

    def test_to_json_string(self):
        """
        Tests the to_json_string static method.
        """
        r = Rectangle(3, 4, 1, 2, 12)
        d = r.to_dictionary()

        r1 = Rectangle(5, 6, 0, 1, 90)
        d1 = r1.to_dictionary()

        json_string = Rectangle.to_json_string([d, d1])
        d2 = ('[{"x": 1, "y": 2, "id": 12, "height": 4, "width": 3}, '
              '{"x": 0, "y": 1, "id": 90, "height": 6, "width": 5}]')
        self.assertEqual(json_string, d2)

        empty1 = Rectangle.to_json_string([])
        self.assertEqual(empty1, '[]')

        empty2 = Rectangle.to_json_string(None)
        self.assertEqual(empty2, '[]')

    def test_from_json_string_with_valid_objs(self):
        """
        Tests the from_json_string static method.
        """
        r = Rectangle(2, 3, 0, 0, 10)
        r1 = Rectangle(4, 5, 0, 0, 9)

        d = r.to_dictionary()
        d1 = r1.to_dictionary()

        json_string = Rectangle.to_json_string([d, d1])

        obj = Rectangle.from_json_string(json_string)
        obj1 = [{"x": 0, "y": 0, "id": 10, "width": 2, "height": 3},
                {"x": 0, "y": 0, "id": 9, "width": 4, "height": 5}]
        self.assertEqual(obj, obj1)

    def test_from_json_string_none(self):
        """
        Tests the from_json_string static method.
        Pssing an empty list or None to the method.
        Expecting an empty list.
        """
        empty = Rectangle.from_json_string(None)
        empty1 = Rectangle.from_json_string('[]')

        self.assertEqual(empty, [])
        self.assertEqual(empty1, [])


class TestSaveToFile(unittest.TestCase):
    """
    Class: TestSaveToFile

    Contains methods that test the save_to_file class method
    in superclass Base.
    """

    # set up method that ensures the file is removed if it exists,
    # before each test is run.
    def setUp(self):
        """
        This method ensures that the file with that file name is removed
        or deleted before each test is run.
        """
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')

    def test_save_to_file_with_objects(self):
        """
        Tests whether save_to_file successfully writes objects
        to a file.
        """

        r1 = Rectangle(10, 20)
        r2 = Rectangle(5, 8)
        Rectangle.save_to_file([r1, r2])

        # check if the file has been created
        self.assertTrue(os.path.exists('Rectangle.json'))

        # chaeck that it is not empty
        self.assertNotEqual(os.path.getsize('Rectangle.json'), 0)

    def test_save_to_file_with_none(self):
        """
        Tests whether save_to_file successfully writes '[]'
        if argument is None.
        """
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists('Rectangle.json'))

        with open('Rectangle.json', mode='r', encoding='utf-8') as r:
            bytess = r.read()

        self.assertEqual('[]', bytess)

    def test_save_to_file(self):
        """
        Tests whether save_to_file successfully writes '[]'
        if argument is [].
        """
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists('Rectangle.json'))

        with open('Rectangle.json', mode='r', encoding='utf-8') as r:
            bytess = r.read()

        self.assertEqual('[]', bytess)


class TestCreate(unittest.TestCase):
    """
    Class: TestCreate
    Contains methods for testing the create class method.
    """

    def test_create(self):
        """
        Tests the create class method.
        """

        r1 = Rectangle(2, 6, 1, 2, 12)

        d1 = r1.to_dictionary()
        obj = Rectangle.create(**d1)
        obj = obj.to_dictionary()

        self.assertEqual(obj, d1)

    def test_create_with_empty_dict(self):
        """
        Tests outcome of passing empty dict to create method.
        """

        with self.assertRaises(AttributeError):
            d = {}
            obj = Rectangle.create(**d)
            obj = obj.to_dictionary()

    def test_excess_args(self):
        """
        Tests excess args passed to create method.
        """
        r1 = Rectangle(2, 6, 1, 2, 12)
        d1 = r1.to_dictionary()

        with self.assertRaises(TypeError):
            obj = Rectangle.create(10, **d1)


class TestLoad(unittest.TestCase):
    """
    Class: TestLoad

    Contains methods that test the load_from_file class
    method.
    """
    def setUp(self):
        """
        This method ensures the file we want to load from is removed,
        if it exists,
        before each test is run.
        """
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')

    def tearDown(self):
        """
        This method cleans up after the test.
        """

    def test_file_exists(self):
        """
        Test load_from_file with an existing file.
        """
        r = Rectangle(3, 4)
        r1 = Rectangle(2, 5)
        d = r.to_dictionary()
        d1 = r1.to_dictionary()
        list_of_dicts = [d, d1]

        with open('Rectangle.json', encoding='utf-8', mode='w') as f:
            f.write(Rectangle.to_json_string(list_of_dicts))

        list_of_objs = Rectangle.load_from_file()
        list_of_objs = [obj.to_dictionary() for obj in list_of_objs]
        self.assertEqual(list_of_objs, list_of_dicts)

    def test_file_nonexistent(self):
        """
        Tests load_from_file against a non existent file.
        Should return []
        """
        empty = Rectangle.load_from_file()
        self.assertEqual(empty, [])

    def test_too_many_args(self):
        """
        Tests for excess arguments passed to load_from_file.
        """

        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1)

        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1, 2)


if __name__ == "__main__":
    unittest.main()
