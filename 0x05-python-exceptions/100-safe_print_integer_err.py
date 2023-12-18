#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as Err:
        # use the file=sys.stderr parameter to direct output
        # to stderr instead of stdout
        print("Exception: {}".format(Err), file=sys.stderr)
        return False
