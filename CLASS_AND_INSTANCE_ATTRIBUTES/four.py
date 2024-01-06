#!/usr/bin/python3
# let us tyr omitting self in this example
# still does not solve our problem.
class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def Instances():
        return Robot.__counter
