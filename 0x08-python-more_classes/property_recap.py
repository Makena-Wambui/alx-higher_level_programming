#!/usr/bin/python3

class P:

    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

if __name__ == "__main__":
    a = P(1001)
    print(a.x)
    a.x = -1
    print(a.x)



class Robot:
    """This class has internal attributes which can not be accessed 
    from outside.
    These are the private attributes: self.__potential_physical
    and self.__potential_psychic.
    We show that a property can be deduced from the values of more
    than one property.
    The property condition, returns the condition of our robot in
    a descriptive string.
    It depends on the sum of the values of psychic and physical conditions of 
    the robot."""

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        c = self.__potential_physical + self.__potential_psychic
        if c <= -1:
            return "Miserable!"
        if c <= 0:
            return "Bad!"
        if c <= 0.5:
            return "Meeeh"
        if c <= 1:
            return "I am ok!"
        else:
            return "aMazing!"


if __name__ == "__main__":
   x = Robot("Elsa", 2000, 0.2, 0.4)
   y = Robot("Patrick", 1980, -0.4, 0.3)
   print(x.condition)
   print(y.condition)
