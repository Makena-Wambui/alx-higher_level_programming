#!/usr/bin/python3

class Pet:
    _class_info = "pet animals"

    # this method is now defined as a static method
    @staticmethod
    def about():
        print("This class is about {}!".format(Pet._class_info))



#this class Dog is a subclass of the class Pet.
# it inherits the method about from the class Pet
class Dog(Pet):
        _class_info = "man's best friend!"

class Cat(Pet):
        _class_info = "all kinds of cats"


if __name__ == "__main__":
    Pet.about()
    Dog.about()
    Cat.about()
