#!/usr/bin/python3
class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def Instances(self):
        return Robot.__counter


if __name__ == '__main__':
    # print("{}".format(Robot.Instances()))
    x = Robot()
    print("{}".format(x.Instances()))
    y = Robot()
    print("Number of class objects: {}".format(x.Instances()))
    print("{}".format(Robot.Instances(x)))

"""why this is not a good idea?
You can not inquire the number of Robots without first creating an instance.
If we try to invoke the method using the class name,
we get an error message because it needs an instance as an argument."""
