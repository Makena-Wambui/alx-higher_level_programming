#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0  # let us keep track of the number of elements being printed
    for value in range(x):
        try:
            print("{}".format(value), end="")
            number += 1
        except IndexError:  # index in the list that is out of range
            break
    print()
    return number
