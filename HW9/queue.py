"""
Filename:       queue.py
Description:    Assignment for Lab 6 of CSCI 603

                This module contains the implementation of the queue data
                structure for storing vertex objects.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from linked_node import LinkedNode
from vertex import Vertex


class Queue:
    """
    Implementation of a queue data structure that stores Vertex objects.
    """

    __slots__ = (
        "_front",   # vertex at the front of the queue
        "_back"     # vertex at the back of the queue
    )

    def __init__(self):
        """
        An initializer for the Queue class.
        """
        self._front = None
        self._back = None

    def is_empty(self) -> bool:
        """
        Checks if this queue is empty.

        :return:        true if the queue is empty; else false
        """
        return self._back is None

    def enqueue(self, vertex: Vertex) -> None:
        """
        Adds a vertex to the rear of this queue.

        :return:        None
        """
        node = LinkedNode(vertex)

        if self._front is None:

            # queue is currently empty
            self._front = node
        else:
            self._back.link = node

        self._back = node

    def dequeue(self) -> Vertex:
        """
        Removes and returns the vertex object at the front of this queue.

        :return:        vertex object at the front of this queue
        """
        assert not self.is_empty()

        vertex = self._front.vertex

        self._front = self._front.link

        if self._front is None:
            self._back = None

        return vertex
