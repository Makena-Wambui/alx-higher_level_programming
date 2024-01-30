#!/usr/bin/python3

class MyClass:

    def __init__(self, x):
        self.OurAtt = x
    
    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, y):
        if y < 0:
            self.__OurAtt = 0
        elif y > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = y


if __name__ == "__main__":
    a = MyClass(10)
    print(a.OurAtt)
    a.OurAtt = -9
    print(a.OurAtt)


