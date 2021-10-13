"""
Filename:       gate.py
Description:    Assignment for Lab 6 of CSCI 603

                This module contains the implementation of an gate at the
                airport.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""
from aircraft import Aircraft
from passenger import Passenger
from zone import Zone


class Gate:
    """Class to define an airport gate."""

    __slots__ = (
        "_zones",  # the list of zone objects to represent the boarding zones
        "_max_capacity"  # the maximum number of passengers allowed in this gate
    )

    def __init__(self, max_capacity: int):
        """
        Creates a Gate object.

        @param max_capacity:        the maximum number of passengers allowed
                                    in this gate
        """

        self._max_capacity = max_capacity

        # initialize the boarding zones
        self._zones = []
        for i in range(4):
            self._zones.append(Zone(i + 1))

    def get_current_pax_count(self) -> int:
        """
        Returns the total number of people currently lined up in the gate.

        :return:        the total number of people currently lined up
                        in the gate
        """

        total_pax = 0
        for zone in self._zones:
            total_pax += zone.get_pax_count()

        return total_pax

    def add_pax(self, passenger: Passenger) -> None:
        """
        Adds a passenger to this gate.

        @param passenger:       passenger to be added
        @return:                None
        """

        if self.get_current_pax_count() + 1 > self._max_capacity:
            return False

        # get the boarding zone number of the passenger
        zone = passenger.get_zone()

        # add the passenger to the corresponding zone
        self._zones[zone - 1].add_pax(passenger)

        if self.get_current_pax_count() == self._max_capacity:

            # maximum capacity has been reached
            return False

        # there's still space for more pax
        return True

    def board_pax(self, aircraft: Aircraft) -> None:
        """
        Boards the passengers in this gate to the aircraft.

        @param aircraft:        aircraft to which passengers are to be boarded
        @return:
        """

        print("Passengers are boarding the aircraft...")
        for i in range(4):
            zone = self._zones[3 - i]
            while zone.get_pax_count() != 0 and not aircraft.is_full():
                pax = zone.remove_pax()
                print(pax)
                aircraft.board(pax)

        if aircraft.is_full():
            print("The aircraft is full.")
        else:
            # all pax in the gate were boarded
            print("There are no more passengers at the gate.")

        print("Ready for taking off ...")

    def is_empty(self) -> bool:
        """
        Checks whether the gate is empty.

        @return:            True if the gate is empty. Else returns False.
        """

        return self.get_current_pax_count() == 0
