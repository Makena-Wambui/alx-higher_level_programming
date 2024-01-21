#!/usr/bin/python3
import unittest
from Circle_Area import Area
from math import pi
"""This module contains tests for the Area function,
which computes the area of a circle.
"""
# create a class that is a subclass of the test case class in the unittest module.
class TestArea(unittest.TestCase):
    # write the test methods inside this class.
    # each test method inside his class must start with the word test.
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(Area(1), pi)
        # first value is the output of the Area function and
        # the second value is the correct answer.
        self.assertAlmostEqual(Area(0), 0)
        self.assertAlmostEqual(Area(2.1), (pi * (2.1 ** 2)))

    # let us now test the function to see that it handles improper inputs corresctly.
    def testValues(self):
        # raise valueerrors when necessary eg for negative numbers.
        # use assertraises method to ensure an exception is raised.
        self.assertRaises(ValueError, Area, -6)

    def testTypes(self):
        self.assertRaises(TypeError, Area, 2 + 5j)
        self.assertRaises(TypeError, Area, True)
        self.assertRaises(TypeError, Area, "kite")

