#!/usr/bin/python3

"""This is the base class.
Note object in parentheses.
Generally, object is the ancestor of all classes.
In Python 3.x, class Person and class Person(object)
are equivalent.
"""
class Person(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):

    def isEmployee(self):
        return True

if __name__ == "__main__":
    emp = Person("Tyson") # an object of Person
    print(emp.getName(), emp.isEmployee())

    emp = Employee("Gift") # an object of Employee
    print(emp.getName(), emp.isEmployee())
