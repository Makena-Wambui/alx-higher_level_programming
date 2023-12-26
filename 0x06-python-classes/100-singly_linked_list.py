#!/usr/bin/python3
"""This module contains the definition of the class Node and
"""


class Node:
    """Each instance of this class is initialized with the
    private attributes data and next_node.
    Attributes:
        data
        next_node

    Properties:
        data
        next_node

    Setters:
        data
        next_node
    """
    def __init__(self, data, next_node=None):
        """This magic method is called every time an instance
        of class Node is created.
        Each node object has the data part which is an integer
        and the next_node which contains the address of the next node."""

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """This property data retrieves the value of the attribute data."""
        return self.__data

    @data.setter
    def data(self, value):
        """The property setter data sets the attribute data to value."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This property returns the value of the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This property setter sets the value of the attribute
        next_node to value.
        None is a data type and an object of the NoneType Class."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """Additional str method for printing a Node object."""
        return str(self.__data)


class SinglyLinkedList:
    """This class defines a singly linked list."""
    def __init__(self):
        """Each instance is initialized with the private attribute head.
        Head here refers to the head node, which is usually None, ie
        empty list."""
        self.__head = None

    def sorted_insert(self, value):
        """This method inserts a new Node into the correct
        sorted position in the list (increasing order).
        Value is the new node to insert."""

        # let us create a new Node object to insert into the list.
        new_node = Node(value)
        temp = self.__head

        # if there are no nodes in the list.
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        # if the existing nodes data has a higher value than the incoming node.
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node

            # insert the node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """We define this special method so we can be able to print
        using print() a SinglyLinkedList object."""
        the_list = ""
        temp = self.__head
        while temp is not None:
            the_list += str(temp.data) + '\n'
            temp = temp.next_node
        return the_list.rstrip()
