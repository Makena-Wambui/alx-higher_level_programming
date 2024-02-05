#!/usr/bin/python3

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class Student(Person):

    def __init__(self, name, age, dob):
        super().__init__("Rahul", age)
        self.sname = name
        self.sage = age
        self.dob = dob
        #super().__init__("Rahul", age)

    def s_display(self):
        print(self.sname, self.sage, self.dob)

if __name__ == "__main__":
    a = Student("Mayan", 32, "20/08/1991")
    a.display()
    a.s_display()
