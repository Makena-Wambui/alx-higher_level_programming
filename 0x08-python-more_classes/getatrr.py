#!/usr/bin/python3
"""
The process of creating getters and setters involves repetitive
patterns.
Instead let us employ generic getters and setters.
let us use __getattr__ and __setattr__ to manage our attributes.
They are invoked automatically when attribute access or assignment
occurs on an object.
"""

class Robot:

    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    def __getttr__(self, name):
        return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        # if certain conditions have to be met
        if name == 'name':
            if value in ['Archer', 'Titan']:
                raise ValueError("Not a valid name")
        if name == 'build_year':
            if value < 2020:
                raise Exception("Build year must be beyond 2019.")

        self.__dict__[f"__{name}"] = value




if __name__ == "__main__":
    x = Robot("Jason", 2021, "Chicago")
    print(x.__dict__)
    print(x.__name)
    y = Robot("Henry", 2019, "Nairobi")
    print(y.__city)
    print(y.__buid_year)
