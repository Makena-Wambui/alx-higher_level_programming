#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # create a listof keys that have that value we want to delete
    KEYS = [key for key, val in a_dictionary.items() if val is value]
    # then iterate through KEYS
    for i in KEYS:
        del a_dictionary[i]
    return a_dictionary
