#!/usr/bin/python3
"""square module."""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
    - __data (int): The data of the node.
    - __next_node (Node or None): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
        - data (int): The data of the node.
        - next_node (Node or None, optional): The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
        - int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Args:
        - value (int): The data to set.

        Raises:
        - TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
        - Node or None: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Args:
        - value (Node or None): The next node to set.

        Raises:
        - TypeError: If next_node is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
    - __head: The head of the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
        - value (int): The value to insert.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the entire list.

        Returns:
        - str: The string representation of the list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")
