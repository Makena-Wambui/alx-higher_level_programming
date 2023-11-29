#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end="")
'''
ord function in python returns the integer representation
of a character according to the Unicode std.
chr function will then convert each integer to back to its corresponding char
to remove the newline added automatically by print, use the end parameter.
'''
