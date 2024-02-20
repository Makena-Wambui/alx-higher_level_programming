#!/usr/bin/python3

"""
This is the 100-append_after module
It supplies one function:
    append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function: append_after

    Args
    -----
        filename

        search_string = string in any line of the file.
        if that string is present,
        then insert the new_string after that line that contains that
        particular search string.

        new_string: string we are appending to each line taht contains the
        search string.
    """

    # let us open the file for reading
    file =''
    with open(filename, encoding='utf-8') as f:
        for line in f:
            file = file + line

            if search_string in line:
                file = file + new_string

    # now we open the file for writing
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(file)
