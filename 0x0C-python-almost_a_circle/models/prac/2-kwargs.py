#!/usr/bin/python3

def greet(name, age):
    print(f"Hi {name}. You are {age} years old.")

if __name__ == "__main__":
    kwargs = {"name": "Jake", "age": 7}
    greet(**kwargs)
