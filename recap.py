#!/usr/bin/python3

class A:
    counter = 0
    def __init__(self):
        type(self).counter += 1
    def __del__(self):
        type(self).counter -= 1


if __name__ == "__main__":
    a = A()
    print("No of instances: {}".format(a.counter))

    b = A()
    print("No of instances: {}".format(a.counter))

    del a
    print("No of insatnces: {}".format(A.counter))

    del b
    print("No of insatnces: {}".format(A.counter))
