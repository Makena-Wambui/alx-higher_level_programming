#!/usr/bin/python3

if __name__ == "__main__":
    width, height = input().split()

    for row in range(int(height)):
        for column in range(int(width)):
            print('#', end='')
        print()
