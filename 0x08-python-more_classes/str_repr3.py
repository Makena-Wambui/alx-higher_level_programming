#!/usr/bin/python3

class A:

    def __repr__(self):
        return 'dad'


if __name__ == "__main__":
    a = A()
    print(a)
    print(str(a))
    print(repr(a))
