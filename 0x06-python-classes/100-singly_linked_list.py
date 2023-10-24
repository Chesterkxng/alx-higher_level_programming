#!/usr/bin/python3
"""
module that act like a singly linked list
"""


class Node:
    """ the class for Node """
    def __init__(self, data, next_node=None):
        """ initialization of Node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ get the node data """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ setter to the node """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ get the next node """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ set the next node """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class singly Linked List """

    def __init__(self):
        """ Initialize class """
        self.head = None

    def __str__(self):
        """To string """
        string = ""
        node = self.head
        while node:
            string += str(node.data) + '\n'
            node = node.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Inserts a new node at the right position"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new_node.next_node = node.next_node
        node.next_node = new_node
