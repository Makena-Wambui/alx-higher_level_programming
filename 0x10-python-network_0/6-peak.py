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

    # if all elements are the same
    if all(x == list_of_integers[0] for x in list_of_integers):
        return list_of_integers[0]
    # the index of the first element in the array.
    low = 0

    # so we dont go out of bounds of the array
    n = len(list_of_integers) - 1

    while low <= n:
        # define our mid point
        mid = (low + n) // 2

        # element to the left of mid
        mid_l = list_of_integers[mid - 1] if mid - 1 > 0 else float("-inf")

        # element to the right of mid
        mid_r = list_of_integers[mid + 1] \
            if mid + 1 < len(list_of_integers) else float("inf")

        if mid_l < list_of_integers[mid] and mid_r < list_of_integers[mid]:
            return list_of_integers[mid]
        elif mid_l > list_of_integers[mid]:
            n = mid - 1
        else:
            low = mid + 1
