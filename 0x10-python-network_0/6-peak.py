#!/usr/bin/python3

"""
This module supplies one function: find_peak
"""


def find_peak(list_of_integers):
    """
    This fuction finds the peak in a list of integers.
    """

    if len(list_of_integers) == 0:
        return None

    n = len(list_of_integers) - 1

    for i in range(0, n):
        if list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]

    return list_of_integers[n]
