#!/usr/bin/python3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if 1 <= a <= 10 ** 10 and 1 <= b <= 10 ** 10:
        print("{}".format(a + b))
        print("{}".format(a - b))
        print("{}".format(a * b))
    else:
        print("Input out of bounds.")
