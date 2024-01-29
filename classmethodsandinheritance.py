#!/usr/bin/python3

#demonstarte the usefulness of class methods in inheritance

class Pet:
    _class_info = "pet animals"

    # this method, which is an instance method, gives some general class info.
    def about(self):
        print("This class is about {}!".format(self._class_info))
    #this class Dog is a subclass of the class Pet.
    # it inherits the method about from the class Pet
class Dog(Pet):
        _class_info = "man's best friend!"

class Cat(Pet):
        _class_info = "all kinds of cats"


if __name__ == "__main__":
    horse = Pet()
    horse.about()
    buddy = Dog()
    buddy.about()
    pickles = Cat()
    pickles.about()
    Pet.about(horse)
"""
In the above example we had to dreate instances of Pet, Dog and Cat
inorder to know what the class is all about.
This is awful design.
It would be better if we could write Pet.about() or Cat.about()
or Dog.about() inorder to get the output we desired.
But we cant do this because about is an instance method and we must create
an object in order to access it.
But we acn also write Pet.about(horse), Dog.about(buddy) or Cat.about(pickles)."""


