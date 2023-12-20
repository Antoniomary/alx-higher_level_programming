#!/usr/bin/python3
"""a class definition"""


class Node:
    """ defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieves the data"""

        return self.__data

    @data.setter
    def data(self, value):
        """sets the value of data"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """retrieves the next_node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node"""

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the
        list (increasing order)
        """

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif new_node.data < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node and temp.next_node.data < new_node.data:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """gives list printability"""

        temp = self.__head
        linked_list = ""
        while temp:
            linked_list += str(temp.data)
            if temp.next_node is not None:
                linked_list += "\n"
            temp = temp.next_node
        return linked_list
