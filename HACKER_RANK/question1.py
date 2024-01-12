#!/usr/bin/python3
# import math
# import os
# import random
# import re
# import sys


if __name__ == '__main__':
    n = int(input().strip())
    """
    when you use input function, you do not have to include a message.
    even by itself, it will prompt the user to enter a value.
    it will wait for the user's input.
    the input is then stored in the variable n.

    strip() method will remove any leading or trailing whitespaces
    from the input."""

    if 1 <= n <= 100:
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0 and 2 <= n <= 5:
            print("Not Weird")
        elif n % 2 == 0 and 6 <= n <= 20:
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")
    else:
        print("Please enter a number between 1 and 100.")
