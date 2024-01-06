#!/usr/bin/python3
class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


if __name__ == '__main__':
    x = C()
    print("The number of instances is: {}".format(C.counter))
    y = C()
    print("The number of instances is: {}".format(C.counter))
    del x
    print("The number of instances is: {}".format(C.counter))
    del y
    print("The number of instances is: {}".format(C.counter))
