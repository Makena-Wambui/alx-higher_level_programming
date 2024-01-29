#!/usr/bin/python3

# demonstrate that class methods are the best methods to use in inheritance.

class Pet:
    _class_info = "pet animals."

    @classmethod
    def about(cls):
        print("This class is about {}".format(cls._class_info))

class Dog(Pet):
    _class_info = "man's best friend!"

class Cat(Pet):
    _class_info = "all kinds of cats."


if __name__ == "__main__":
    Pet.about()
    Dog.about()
    Cat.about()
