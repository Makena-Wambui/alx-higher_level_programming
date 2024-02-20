#!/usr/bin/python3
"""
This is a script that adds all arguments to a Python list,
and then saves them to a file.
"""

import sys
"""
sys.argv is a list in Python.
It contains all the command line arguments
passed to the script.
sys.argv[0] contains the name of the script.
subsequent elements are the user applied arguments.
sys.argv[1:] slicing selects all arguments excluding the name of the script,
ie it includes all arguments to the end.
"""

if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file

    try:
        obj = load_from_json_file('add_item.json')
    except Exception as err:
        obj = []
    for arg in sys.argv[1:]:
        obj.append(arg)
    save_to_json_file(obj, 'add_item.json')
