#!/usr/bin/python3

def test_args(f_arg, *args):
    print("First argument is : ", f_arg)

    for a in args:
        print("More arguments: ", a)

if __name__ == "__main__":
    test_args("mom", "dad", 3, {1, 2})
