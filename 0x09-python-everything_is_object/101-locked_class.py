#!/usr/bin/python3

"""
This is the 101-locked_class module.
It supplies one class:
    LockedClass
EXPLANATION:
------------
Slots is only used in the context of Python classes.
It is a class variable.
It is usually assigned a sequence
of strings, that are variable names used by instances.
Python reserves space for them in memory,
and prevents creation of __dict__ and __weakref__
attributes.
Also prevents creation of any variables that are not declared in
__slots__
"""


class LockedClass:
    """
    This is the class LockedClass.
    No class or object attributes
    No methods
    Prevents the user from dynamically creating any
    New instance attributes,
    unless if the new instance attribute is
    first_name.
    """
    __slots__ = ('first_name')
