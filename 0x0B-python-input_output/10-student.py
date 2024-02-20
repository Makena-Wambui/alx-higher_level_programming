#!/usr/bin/python3

"""
This is the 10-student module.
It supplies one class:
    Student.
"""


class Student:
    """
    This is the class Student.

    Public instance variables:
        first_name = first_name
        last_name = last_name
        age = age
    Instance methods:
        __init__
        to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        This is the Python Constructor method.
        It is called automatically each time the class is instantiated.
        It initializes the insance variables first_name, last_name
        and age to the values of the respective parameters.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This is a public instance method.
        It retrieves a dictionary representation of a
        Student object.

        Attrs: list of strings.
            Represents the attribute names whose values we want to retrieve
        """
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

        else:
            return self.__dict__
