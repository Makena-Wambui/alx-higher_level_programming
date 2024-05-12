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

    low = 0

    # so we dont go out of bounds of the array
    n = len(list_of_integers) - 1

    while low < n:
        # define our mid point
        mid = (low + n) // 2

        # Check if mid is a peak
        if (mid == 0 or
                list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or
           list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the element to the right of mid is greater, peak is to the right
        elif mid < len(list_of_integers) - 1 and \
                list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1

        # Otherwise, peak is to the left
        else:
            n = mid
    # Return the remaining element if it's a peak
    return list_of_integers[low]
