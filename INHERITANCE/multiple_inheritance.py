#!/usr/bin/python3

class Base1():
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")

class Base2():
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

class Child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
        self.str1 = "Geek3"
        self.str3 = "Geek4"

    def printer(self):
        print(self.str1, self.str2, self.str3)

if __name__ == "__main__":
   a = Child()
   a.printer()
