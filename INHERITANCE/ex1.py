#!/usr/bin/python3

class Person(object):

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def display(self):
        print("{}, {}".format(self.name, self.ID))


#if __name__ == "__main__":
    #emp1 = Person("Alicia", "3000")
    #emp1.display()

# let us create a subclass Emp that inherits from base class Person
class Emp(Person):

    def Print(self):
        print("Emp class called.")


if __name__ == "__main__":
    emp2 = Emp("Taylor", 1000)

    #this object can call the parent class function.
    emp2.display()
    # it can also call the child class function.
    emp2.Print()
