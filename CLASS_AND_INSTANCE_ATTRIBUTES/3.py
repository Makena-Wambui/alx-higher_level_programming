#!/usr/bin/python3
from two import Robot
for number, law in enumerate(Robot.Three_Laws):
    print("{}:\n {}\n".format(number + 1, law))
