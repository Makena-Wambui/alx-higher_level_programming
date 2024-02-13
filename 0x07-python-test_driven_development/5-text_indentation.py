#!/usr/bin/python3

"""
This is the ===5-text_indentation module===
It supplies one function: text_indentation.
"""


def text_indentation(text):
    """Prints input text with 2 new lines after each
    of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # let us iterate through each character in the characters provided
    for c in ".:?":
        # replace all occurences of tht character with that character
        # followed by two new lines.
        text = (c + "\n\n").join([line.strip(" ") for line in text.split(c)])
        """split the text into a list of strings,
        using the character c as the separator.
        iterate through each line in that list and use strip
        to remove leading or tarailing whitespaces.
        then join the strings back together using the character c
        and two new lines.
        """
    print("{}".format(text), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
