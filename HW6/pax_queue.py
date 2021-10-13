"""
Filename:       pax_queue.py
Description:    Assignment for Lab 6 of CSCI 603

                This module contains the implementation of the queue data
                structure for storing passenger objects.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from linked_node import LinkedNode
from passenger import Passenger


class PaxQueue:
    """
    Implementation of a queue data structure that stores Passenger objects.
    """

    __slots__ = (
        "_front",   # passenger at the front of the queue
        "_back"     # passenger at the back of the queue
    )

    def __init__(self):
        """
        An initializer for the PaxQueue class.
        """
        self._front = None
        self._back = None

    def is_empty(self) -> bool:
        """
        Checks if this queue is empty.

        :return:        true if the queue is empty; else false
        """
        return self._back is None

    def enqueue(self, passenger: Passenger) -> None:
        """
        Adds a passenger to the rear of this queue.

        :return:        None
        """
        node = LinkedNode(passenger)

        if self._front is None:

            # queue is currently empty
            self._front = node
        else:
            self._back.link = node

        self._back = node

    def dequeue(self) -> Passenger:
        """
        Removes and returns the passenger object at the front of this queue.

        :return:        passenger object at the front of this queue
        """
        assert not self.is_empty()

        pax = self._front.passenger

        self._front = self._front.link

        if self._front is None:
            self._back = None

        return pax
