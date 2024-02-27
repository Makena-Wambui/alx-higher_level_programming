#!/usr/bin/python3

"""
This is the test_base module.
It contains tests for the Base Class.
"""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """
    Class: TestBase

    Tests the Base Class.

    A subclass of unittest.TestCase

    Methods:
    test_id
    test_nb_objects
    test_too_many_arguments
    """
    def test_id(self):
        """
        Method: test_id

        Tests the id attribute of the Base Class.
        """

        q1 = Base()
        self.assertEqual(q1.id, 1)
        # if i pass None to Base

        q = Base(None)
        self.assertEqual(q.id, 2)

        # instantiate with id = 12
        b = Base(12)
        # expect id to be 12
        self.assertEqual(b.id, 12)

        b1 = Base()
        # expect id = 2
        self.assertEqual(b1.id, 3)

        b2 = Base()
        # expect id = 3
        self.assertEqual(b2.id, 4)

        b3 = Base(-2)
        # expect id = -2
        self.assertEqual(b3.id, -2)

    def test_nb_objects(self):
        """
        Method:
            test_nb_objects.

        Tests the __nb_objects attribute
        """
        a = Base(90)
        with self.assertRaises(AttributeError):
            a.__nb_objects

        self.assertEqual(a._Base__nb_objects, 4)

        b = Base(None)
        self.assertEqual(a._Base__nb_objects, 5)

        c = Base(30)
        self.assertEqual(a._Base__nb_objects, 5)

        d = Base()
        self.assertEqual(a._Base__nb_objects, 6)

    def test_too_many_arguments(self):
        """
        Method:
            test_too_many_arguments
        Test number of arguments passed to Base
        """
        self.assertRaises(TypeError, Base, 3, 4)


if __name__ == "__main__":
    unittest.main()
