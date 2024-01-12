#!/usr/bin/python3
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 20:
        for i in range(n):
            print("{}".format(i ** 2))
    else:
        print("Input is out of bounds.")
