#!/usr/bin/python3

class Parent:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello I am {self.name} from the Parent class"

class Child(Parent):
    def __init__(self, name, age):
        # lets call the parent class constructor method
        super().__init__(name)
        self.age = age

    def greet(self):
        # use super to access the parent class method greet
        greeting = super().greet()
        return f"{greeting} ad i am {self.age} years old"


if __name__ == "__main__":
    obj = Child("Jake", 7)
    print(obj.greet())
