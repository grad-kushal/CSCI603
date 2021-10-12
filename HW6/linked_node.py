"""
Filename:       lineked_node.py
Description:    Assignment for Lab 5 of CSCI 603

                This module contains the class to represent the node in a
                passenger stack of queue that holds a passenger object.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from passenger import Passenger


class LinkedNode:
    """
    Class to represent the node in a passenger stack of queue that holds a
    passenger object.
    """

    __slots__ = "passenger", "link"

    def __init__(self, passenger: Passenger, link=None):
        """
        An initializer for the LinkedNode object.
        """
        self.passenger = passenger
        self.link = link

    def __str__(self) -> str:
        """
        String representation of this object.
        
        :return:        the string representation of this object
        """
        return str(self.passenger)
