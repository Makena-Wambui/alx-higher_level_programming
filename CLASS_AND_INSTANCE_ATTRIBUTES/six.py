#!/usr/bin/python3
class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1
    
    @staticmethod
    def Instances():
        return Robot.__counter


if __name__ == '__main__':
    print("{}".format(Robot.Instances()))
    x = Robot()
    print("{}".format(x.Instances()))
    y = Robot()
    print("{}".format(y.Instances()))
    print("{}".format(Robot.Instances()))
