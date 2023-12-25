#!/usr/bin/python3
# printing a solid square in Python
# ask for user input and convert t
# int.
print("Solid Square")
size = int(input("Enter the number of rows: "))
if size == 0:
    print()
else:
    for i in range(size):
        print('#' * size)
