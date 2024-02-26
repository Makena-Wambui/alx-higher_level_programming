#!/usr/bin/python3

"""
This is the base module.
It supplies one class:
    Base
"""

import json
import turtle


class Base:
    """
    Class: Base

    Private class attribute:
    __nb_objects

    Public Instance Attribute:
    id

    Method:
    __init__
    to_json_string
    save_to_file
    from_json_string
    create

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Magic method: __init__

        Automatically called each time the class is
        instantiated.
        If id is not none, it sets the value of id to the value
        of the argument, id.

        else, __nb_objects is incremented,
        and id is assigned the new value of __nb_objects.


        id is always an int so we do not need to test its type.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method: to_json_string

        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method: save_to_file

        Writes the JSON string representation of list_objs to a file

        list_objs: list of Rectangle or list of Square instances

        """
        filename = f"{cls.__name__}.json"

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            # call to_dictionary that returns dict representation
            # of each instance
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]

                # call to_json_string
                json_list = Base.to_json_string(list_dictionaries)
                f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method: from_json_string

        Deserializes json_string.

        json_string is a string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method: create

        Returns an instance with all atrributes set.
        dictionary is a dictionary of attribute names and their values.

        """
        if type(dictionary) is dict and dictionary != {}:
            # first create a dummy instance
            if cls.__name__ == "Rectangle":
                obj = cls(3, 4, 0, 1, 100)
            else:
                obj = cls(2, 1, 3, 10)
            # call update and pass dictionary
            obj.update(**dictionary)

            return obj

    @classmethod
    def load_from_file(cls):
        """
        Class method: load_from_file

        Returns a list of instances.

        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, encoding='utf-8') as f:
                file = f.read()
                lst = Base.from_json_string(file)
                return [cls.create(**d) for d in lst]

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Static method: draw
        Args: 2 lists
        One list contains instances of Rectangle
        The other contains instances of Square

        Uses the Turtle Graphics Module to
        open a window and draws all the Rectangles and Squares
        """

        # Initialize the turtle graphics window
        window = turtle.Screen()

        # setup window with size specifics
        window.setup(width=800, height=600)

        # create a turtle object
        obj = turtle.Turtle()

        # setup TurtleGraphics Settings
        obj.speed(2)

        # draw rectangles
        for r in list_rectangles:
            obj.penup()
            obj.goto(r.x, r.y)
            obj.pendown()
            obj.color("green")

            for a in range(2):
                obj.forward(r.width)
                obj.left(90)
                obj.forward(r.height)
                obj.left(90)
        
        # draw squares
        for s in list_squares:
            obj.penup()
            obj.goto(s.x, s.y)
            obj.pendown()
            obj.color("purple")
            for b in range(4):
                obj.forward(s.size)
                obj.left(90)

        # close Turtle Graphics Window
        window.mainloop()
        turtle.Screen().bye()
