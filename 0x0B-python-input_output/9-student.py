#!/usr/bin/python3

"""
This is the 9-student module.
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
        Method: __init__

        This is the Python Constructor method.
        It is called automatically each time the class is instantiated.

        It initializes the instance variables first_name, last_name
        and age to the values of the respective parameters.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method: to_json

        This is a public instance method.
        It retrieves a dictionary representation of a
        Student object.
        """
        return self.__dict__
