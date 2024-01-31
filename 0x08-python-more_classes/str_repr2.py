#!/usr/bin/python3

class B:

    def __str__(self):
        return 'mom'


if __name__ == "__main__":
    b = B()
    print(b)
    print(str(b))
    print(repr(b))
