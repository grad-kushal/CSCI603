# TODO: Change file name
"""
Filename:       pax_stack.py
Description:    Assignment for Lab 5 of CSCI 603

                This module contains the implementation of the stack data
                structure for storing passenger objects.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from linked_node import LinkedNode
from passenger import Passenger


class PaxStack:
    """
    Implementation of a stack data structure that stores Passenger objects.
    """

    __slots__ = "_top"

    def __init__(self):
        """
        An initializer for the PaxStack class.
        """
        self._top = None

    def is_empty(self) -> bool:
        """
        Checks if this stack is empty.

        :return:        true if the stack is empty; else false
        """
        return self._top is None

    def push(self, passenger: Passenger) -> None:
        """
        Adds a passenger to this stack.

        :return:        None
        """
        new_node = LinkedNode(passenger, self._top)
        self._top = new_node

    def pop(self) -> Passenger:
        """
        Removes and returns the passenger object at the top of this stack.

        :return:        passenger object at the top of this stack
        """
        assert not self.is_empty(), "Popping from an empty stack"

        pax = self._top.passenger

        self._top = self._top.link
        return pax

    def peek(self):
        """
        Returns the passenger object at the top of this stack.

        :return:        passenger object at the top of this stack
        """
        assert not self.is_empty(), "Peeking an empty stack"
        return self._top.passenger

    def __str__(self) -> str:
        """
        String representation of this stack.

        :return:        the string representation of this stack.
        """
        node = self._top
        while node is not None:
            print(str(self._top), " -> ")
            node = node.link
