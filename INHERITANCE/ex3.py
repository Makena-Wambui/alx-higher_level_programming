#!/usr/bin/python3

"""
'object' is written in the declaration of the class Person.
In Python, every class inherits from a built in basic class
called object.
__init__ function ia a constructor method.
it is invoked when we create an object variable
or an instance of the class.
variables defined within __init__ are called instance variables or objects.
name and idnumber are objects of the class Person.
salary and post are objects of the class Employee.
The class Employee inherits from the class Person,
so name and idnumber are also objects of the class Employee.

Let us demonstrate how parent constructors are called.
"""
class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(Person):
    
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoke the parent constructor
        Person.__init__(self, name, idnumber)


if __name__ == "__main__":
    a = Employee("Tom", 3200, 90000, "Manager")
    a.display()
