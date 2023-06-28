#!/usr/bin/python3
"""class Node that defines a node of a singly linked list"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """initialization"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Linked list class"""
    def __init__(self):
        """initialization"""
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            t = self.__head
            while (t.next_node is not None and t.next_node.data < value):
                t = t.next_node
            new.next_node = t.next_node
            t.next_node = new

    def __str__(self):
        strn = []
        tmp = self.__head
        while tmp is not None:
            strn.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(strn)
