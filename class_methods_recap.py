#!/usr/bin/python3

class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter


if __name__ == "__main__":
    print(Robot.RobotInstances())
    a = Robot()
    print(a.RobotInstances())
    b = Robot()
    print(a.RobotInstances())
    print(Robot.RobotInstances())
