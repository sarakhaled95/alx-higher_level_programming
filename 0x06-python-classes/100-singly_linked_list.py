#!/usr/bin/python3
""" node module"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        args:
            data (int): the data of the new node
            next_node (Node): the next node of the new node
        """
        seld.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        """sets the data of the new node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """sets the next node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.next_node = value


class SinglyLinkedList:
    """ defines a singly linked list"""

    def __init__(self):
        """initialize a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the SinglyLinkedList
        the node is inserted in the list in the correct ordered
        numarically
        args:
            value (Node): the new Node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """define the print() representation"""
        values = []
        temp = self.__head
        while temp is not None:
            value.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
