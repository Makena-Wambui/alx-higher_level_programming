#!/usr/bin/python3

class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year


    def __repr__(self):
        return 'Robot("{}", "{}")'.format(self.name, self.build_year)

    def __str__(self):
        return 'Name: {}, Build_Year: {}'.format(self.name, self.build_year)


if __name__ == "__main__":
    x = Robot("Megan", '2000')
    x1 = repr(x)
    print(x1)
    print("Type of x1 is {}.".format(type(x1)))
    x2 = eval(x1)
    print(x2)
    print("Type of x2 is {}.".format(type(x2)))
    print('-------------------------------------')

    y = Robot("Alvin", "2020")
    print(y)
    y2 = str(y)
    print(y2)
    print("Type of y2 is {}.".format(type(y2)))
    #y3 = eval(y2)
    #print(y3)
