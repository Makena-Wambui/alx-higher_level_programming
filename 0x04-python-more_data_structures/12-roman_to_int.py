#!/usr/bin/python3
def roman_to_int(roman_string):
    # check if the string is a valid string or None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # create a dictionary to map Roman numerals and their integer equivalents
    Romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # this is the number that stores the integer value
    number = 0
    # we iterate through the roman string
    for p in range(len(roman_string)):
        # now get the valueof the corrent symbol
        val = Romans.get(roman_string[p])
        # if that value is none, return 0
        if val is None:
            return 0
        # now we check if the current symbol at index
        # is smaller than the next one
        if p < len(roman_string) - 1 and val < Romans.get(roman_string[p + 1]):
            # subtract it
            number = number - val
        else:
            number = number + val
    return number
