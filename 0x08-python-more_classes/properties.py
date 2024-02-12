#!/usr/bin/python3

class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def build_year(self):
        return self.__build_year

    @build_year.setter
    def build_year(self, value):
        self.__build_year = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

if __name__ == "__main__":
    x = Robot("Jason", 1992, "Chicago")
    print(x.name)
    print(x.build_year)
    print(x.city)
