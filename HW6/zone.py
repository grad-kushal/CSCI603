"""
Filename:       zone.py
Description:    Assignment for Lab 6 of CSCI 603

                This module contains the implementation of a boarding zone of a
                gate.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""
from passenger import Passenger
from pax_queue import PaxQueue


class Zone:
    """Class to represent a boarding zone of a gate."""

    __slots__ = (
        "_zone_id",             # zone number
        "_pax_queue",           # passenger queue associated with this zone
        "_current_pax_count"    # number of passengers currently lined up in
                                # this zone
    )

    def __init__(self, zone_id: int):
        """
        An initializer for the zone object.

        @param zone_id:         zone number of this zone
        """
        self._zone_id = zone_id
        self._pax_queue = PaxQueue()
        self._current_pax_count = 0

    def add_pax(self, passenger: Passenger) -> None:
        """
        Adds a passenger to this zone's queue.

        :return:        None
        """
        self._pax_queue.enqueue(passenger)
        self._current_pax_count += 1

    def remove_pax(self) -> Passenger:
        """
        Removes and returns a passenger from this zone.

        :return:        None
        """
        pax = self._pax_queue.dequeue()
        self._current_pax_count -= 1
        return pax

    def get_pax_count(self) -> int:
        """
        Returns the number of passengers currently in this zone's queue.

        :return:        the number of passengers currently in this zone's queue
        """
        return self._current_pax_count
