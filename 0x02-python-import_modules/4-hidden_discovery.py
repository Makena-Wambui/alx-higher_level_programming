#!/usr/bin/python3
import hidden_4
list = dir(hidden_4)
if __name__ == "__main__":
    for name in list:
        if not name.startswith('__'):
            print(name)
