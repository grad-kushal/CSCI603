"""
Filename:       chain_node.py
Description:    Assignment for Lab 7 of CSCI 603

                This module contains the implementation of the chain node class.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from typing import Any


class ChainNode:
    """
    A node to hold (key-value) pair of objects stored in a chained Hash Map
    """
    __slots__ = "key", "value", "link"

    def __init__(self, key: Any, value: Any, link: 'ChainNode' = None):
        """
        A constructor for the ChainNode object.

        @param key:     key
        @param value:   value associated with the key
        @param link:    node next to this one in the chain
        """
        self.key = key
        self.value = value
        self.link = link
