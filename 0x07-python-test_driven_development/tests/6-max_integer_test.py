#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer

"""Create a subclass of the TestCase class from the unittest module."""


class TestMaxInteger(unittest.TestCase):
    """This class contains test methods for the max_integer function.
    Each testing method should start with test_"""
    def test_empty_list(self):
        """This method tests max_integer function with an empty list."""
        my_list = []
        self.assertIsNone(max_integer(my_list), None)
        self.assertIsNone(max_integer(), None)

    def test_listContainsStringElement(self):
        """Method tests for a list that contains ingers and a string."""
        self.assertRaises(TypeError, max_integer, [1, 2, 'School'])

    def test_mixIntsAndFloats(self):
        """Test for a list containing floats and ints."""
        self.assertEqual(max_integer([10.7, 5, 3.4]), 10.7)

    def test_ListOfStrings(self):
        """Method tests for a list of strings only."""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['mom', 'kind', 'type']), 'type')

    def test_OnlyaSingleElement(self):
        """Method tests for a list containing only a single alement."""
        self.assertEqual(max_integer([1]), 1)

    def test_Matrix(self):
        """Method tests for a list containing lists of ints."""
        self.assertEqual(max_integer([[1, 2], [3, 4], [6, 7]]), [6, 7])

    def test_ListwithEqualElements(self):
        """Test for a list that contains elements that are exactly similar."""
        self.assertEqual(max_integer([2, 2]), 2)

    def test_aListofSets(self):
        """Tests for a list of Sets of Integers."""
        self.assertEqual(max_integer([{8, 9}, {6, 7}]), {8, 9})

    def test_ListOfNegatives(self):
        """Test a list containing negative integers"""
        self.assertEqual(max_integer([-1, -2]), -1)

    def test_listofNegativeAndPos(self):
        """Test a list containing positive and negative integers."""
        self.assertEqual(max_integer([2, -1]), 2)

    def test_moreArguments(self):
        """Test for additional arguments passed to the function"""
        self.assertRaises(TypeError, max_integer, 2, 1)

    def test_NoneArgument(self):
        """Test for None passed to function."""
        self.assertRaises(TypeError, max_integer, None)
