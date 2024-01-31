#!/usr/bin/python3

import datetime
today = datetime.datetime.now()
print(today)
str_s = str(today)
# print(eval(str_s))

repr_s = repr(today)
print(repr_s)
t = eval(repr_s)
print(t)
print(type(t))
