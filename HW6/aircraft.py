"""
Filename:       aircraft.py
Description:    Assignment for Lab 5 of CSCI 603

                This module contains the implementation of the AiRIT aircraft.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from pax_stack import PaxStack
from passenger import Passenger
from typing import Optional


class Aircraft:
    """
    Class to represent an aircraft
    """

    __slots__ = (
        "_pax_with_carry_on",     # stack to store pax with carry-on luggage
        "_pax_without_carry_on",  # stack to store pax without carry-on luggage
        "_capacity",              # aircraft's passenger capacity
        "_current_pax"            # number of pax currently in the aircraft
    )

    def __init__(self, capacity: int):
        """
        An initializer for this object.
        """
        self._pax_with_carry_on = PaxStack()
        self._pax_without_carry_on = PaxStack()
        self._capacity = capacity
        self._current_pax = 0

    def board(self, passenger: Passenger) -> bool:
        """
        Board the passenger to this aircraft.

        :return:            True if the passenger has successfully boarded the
                         aircraft. False if the aircraft has reached the maximum
                         capacity.
        """

        if self.is_full():

            # aircraft currently has reached the maximum capacity of passengers
            return False

        if passenger.has_carry_on:
            self._pax_with_carry_on.push(passenger)
        else:
            self._pax_without_carry_on.push(passenger)

        # increment the number of passengers in this aircraft
        self._current_pax += 1

    def deplane(self) -> Optional[Passenger]:
        """
        Deplanes and returns one passenger from the aircraft. The passengers
        will be removed in a last-in-first-out manner, and the passengers
        without a carry-on luggage will be deplaned first.

        :return:            passenger being deplaned. None if no passengers are
                            left to be deplaned.
        """
        if self.is_empty():

            # no passengers to deplane
            return None

        self._current_pax -= 1

        if not self._pax_without_carry_on.is_empty():
            return self._pax_without_carry_on.pop()

        return self._pax_with_carry_on.pop()

    def disembark(self) -> None:
        """
        Deplane all passengers from the aircraft.

        """
        print("Passengers are disembarking..")

        while not self.is_empty():
            pax_deplaned = self.deplane()
            print(pax_deplaned)

    def is_empty(self) -> bool:
        """
        Check whether this aircraft is empty

        :return:        True if the aircraft is empty. Else False.
        """
        if (self._pax_with_carry_on.is_empty()
                and self._pax_without_carry_on.is_empty()):

            # no pax in the plane
            return True

        return False

    def is_full(self) -> bool:
        """
        Check whether this aircraft has reached its maximum capacity.

        :return:        True if the aircraft has reached its maximum capacity.
                        Else False.
        """

        if self._current_pax + 1 <= self._capacity:

            # aircraft currently has reached the maximum capacity of passengers
            return False

        return True
