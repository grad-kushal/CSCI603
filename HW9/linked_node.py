"""
Filename:       lineked_node.py
Description:    Assignment for Lab 9 of CSCI 603

                This module contains the class to represent the node in a
                stack that holds a vertex objects.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from vertex import Vertex


class LinkedNode:
    """Class to represent the node in a stack that holds a vertex objects. """

    __slots__ = "vertex", "link"

    def __init__(self, vertex: Vertex, link=None):
        """
        An initializer for the LinkedNode object.
        """
        self.vertex = vertex
        self.link = link
