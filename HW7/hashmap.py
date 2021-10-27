"""
Filename:       chain_node.py
Description:    Assignment for Lab 7 of CSCI 603

                This module contains the implementation of a chained hash table.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from chain_node import ChainNode
from typing import Any, Callable, Hashable, Optional, List
from collections.abc import Iterable


class HashMap(Iterable):
    """
    A chained hash table that can resize based on the load factor
    (size-to-capacity ratio).
    """
    __slots__ = "size", "table", "load", "load_limit", "hash_function", \
                "capacity"

    def __init__(self,
                 initial_num_buckets: int = 100,
                 load_limit: float = 75.0,
                 hash_func: Callable[[Hashable], int] = hash):
        """
        A constructor for this object.

        @param initial_num_buckets:     the initial number of buckets in this
                                        has table
        @param load_limit:              threshold of load limit beyond which
                                        the hash table should be expanded
        @param hash_func:
        """
        self.capacity = initial_num_buckets
        self.load_limit = load_limit
        self.hash_function = hash_func
        self.table = [None] * initial_num_buckets
        self.size = 0
        self.load = 0  # initial load

    def _get_node_of(self, key: Hashable) -> Optional['ChainNode']:
        """
        Get the ChainNode corresponding to a key.

        @param key:         key of the entry
        @return:            if an entry corresponding to the key exists,
                            then return the ChainNode containing the key;
                            else return None
        """
        bucket = self.hash_function(key) % self.capacity

        # no entry in the bucket
        if self.table[bucket] is None:
            return None
        else:
            current_node = self.table[bucket]

            # check if key is in the first node
            if current_node.key == key:
                return current_node

            while current_node.link is not None:
                current_node = current_node.link
                if current_node.key == key:
                    return current_node

            return None

    def contains(self, key: Hashable) -> bool:
        """
        Check if an entry corresponding to a key is present in the hash table.

        @param key:         key of the entry
        @return:            true if an entry corresponding to a key is present
                            in the hash table; else false
        """
        if self._get_node_of(key) is None:
            return False
        return True

    def _expand_hash_table(self):
        """
        Doubles the capacity of the hash table and re-hashes all elements
        @return:
        """
        new_capacity = 2 * self.capacity
        new_hash_table = [None] * new_capacity
        for key, value in self:
            bucket = self.hash_function(key) % new_capacity

            # prepend to the chain in the bucket
            new_hash_table[bucket] = ChainNode(key,
                                               value,
                                               new_hash_table[bucket])

        self.table = new_hash_table
        self.capacity = new_capacity
        self.load = (self.size * 100) / self.capacity

    def add(self, key: Hashable, value: Any) -> None:
        """
        Insert a new entry into the hash table. If the key
        already exists, the value of that key is updated with the given value.
        Double the size of the table if its load_factor exceeds the load_limit.

        @param key:         key associated with the entry
        @param value:       value associated with the key
        @return:            None
        """

        bucket = self.hash_function(key) % self.capacity

        if not self.contains(key):
            # key not present, prepend to the chain
            self.table[bucket] = ChainNode(key, value, self.table[bucket])
            self.size += 1

        # key already present, find the node in the chain containing
        # the key
        else:
            key_node = self._get_node_of(key)
            key_node.value = value

        # update current load
        self.load = (self.size * 100) / self.capacity

        if self.load > self.load_limit:
            self._expand_hash_table()

    def get(self, key: Hashable) -> Optional[Any]:
        """
        Return the value associated to the given key.

        @param key:         Key to search
        @return:            The value associated to the given key;
                            None if key is not found.
        """
        node = self._get_node_of(key)
        if not node:
            return None
        return node.value

    def remove(self, key: Hashable) -> None:
        """
        Remove an entry from the hash table.

        @param key:         key of the entry to be removed
        @return: 
        """
        bucket = self.hash_function(key) % self.capacity

        # no entry in the bucket
        if self.table[bucket] is None:
            return None
        else:
            current_node = self.table[bucket]

            # check if key is in the first node
            if current_node.key == key:
                self.table[bucket] = current_node.link

            while current_node.link is not None:
                next_node = current_node.link
                if next_node.key == key:
                    current_node.link = next_node.link
                    break
                current_node = next_node

            return None

    def imbalance(self):
        """
        Returns the imbalance factor of the hash table

        @return:        imbalance factor
        """
        num_of_chains = 0
        sum = 0
        for chain in self.table:
            if chain is not None:
                num_of_chains += 1
                while chain is not None:
                    sum += 1
                    chain = chain.link
        return (sum / num_of_chains) - 1

    def __iter__(self):
        """Implementation of iter method for HashMap iterable"""
        i = 0
        while i < self.capacity:
            if self.table[i]:
                current_node = self.table[i]
                while current_node:
                    yield current_node.key, current_node.value
                    current_node = current_node.link
            i += 1
