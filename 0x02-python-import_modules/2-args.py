#!/usr/bin/python3
import sys
if __name__ == '__main__':
    # len(sys.argv) will always include the script name as the first element
    # use length - 1 instead
    length = len(sys.argv)  # will calculate the length of the list
    lis = sys.argv
    if length == 1:
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(length - 1, 's' if length > 2 else ''))
        for a in range(1, length):
            # range 1 to start fro index 1 and ignore name of script
            print("{:d}: {:s}".format(a, lis[a]))
