#!/usr/bin/python3
from four import Robot
# now it is possible to access the method via the class name.
print("{}".format(Robot.Instances()))

# but you can not access that Method via an instance.
x = Robot()
"""print("{}".format(x.Instances())). This is treated as
an instance method call. And an instance method call needs a reference
to the instance as a first parameter.""" 
