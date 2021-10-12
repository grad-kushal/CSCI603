from linked_node import LinkedNode
from passenger import Passenger


class PaxQueue:
    """
    Implementation of a queue data structure that stores Passenger objects.
    """

    __slots__ = "_front", "_back"

    def __init__(self):
        """
        An initializer for the PaxQueue class.
        """
        self._front = None
        self._back = None

    def is_empty(self):
        """
        Checks if this queue is empty.

        :return:        true if the queue is empty; else false
        """
        return self._back is None

    def enqueue(self, passenger: Passenger):

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
