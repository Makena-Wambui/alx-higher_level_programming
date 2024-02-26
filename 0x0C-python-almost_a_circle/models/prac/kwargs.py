#!/usr/bin/python3

def greet(**kwargs):
    if kwargs is not None:
        for k, v in kwargs.items():
            print("{}=={}".format(k, v))

if __name__ == "__main__":
    greet(name="Makena", age=30)
