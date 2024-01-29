#!/usr/bin/python3

class A:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    
    @staticmethod
    def A_Instances():
        return A.__counter 


if __name__ == "__main__":
    print(A.A_Instances())
    d = A()
    print(d.A_Instances())
    f = A()
    print(f.A_Instances())
    print(d.A_Instances())
    print(A.A_Instances())
