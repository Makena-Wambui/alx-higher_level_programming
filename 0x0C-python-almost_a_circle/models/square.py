#!/usr/bin/python3

"""
This is the square module.
It supplies one class:
    Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class: Square

    A subclass of Rectangle.

    Magic methods:
        __init__
        __str__
        update

    Getter: size
    Setter: size


    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class Constructor.

        Called automatically each time the class is instantiated.

        Calls the __init__ of the superclass, Rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Public getter for size.
        Retrieves the value of width attribute.
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        Public setter method size
        """
        super().validator("width", val)
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        Public instance method: update

        Args:
            args - non keyword arguments
            kwargs - key word args
        Assigns attributes.
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                if hasattr(self, k) is True:
                    setattr(self, k, v)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except Exception:
            pass

    def __str__(self):
        """
        Magic method: __str__

        Returns an informal string representation of a Square object.

        """
        return (
                f"[{__class__.__name__}] ({self.id})"
                f" {self.x}/{self.y} - {self.height}"
                )

    def to_dictionary(self):
        """
        Public instance method: to_dictionary

        Returns the dictionary representation of a Square
        """
        return {'id': getattr(self, 'id'), 'x': getattr(self, 'x'),
                'size': getattr(self, 'size'), 'y': getattr(self, 'y')}
