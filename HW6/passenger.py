"""
Filename:       passenger.py
Description:    Assignment for Lab 6 of CSCI 603

                This module contains the implementation of the Passenger class.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""


class Passenger:
    """Class to define a passenger."""
    __slots__ = (
        "name",             # name of the passenger
        "ticket_number",    # ticket number of the passenger
        "has_carry_on"      # whether the pax has a carry on luggage or not
    )

    def __init__(self, name: str,
                 ticket_number: str,
                 has_carry_on: bool = False):
        """
        Creates a passenger object.

        @param name:                name of the passenger
        @param ticket_number:       ticket number of the passenger
        @param has_carry_on:        whether the pax has a carry on luggage
                                    or not
        """

        self.name = name
        self.ticket_number = ticket_number
        self.has_carry_on = has_carry_on

    def __str__(self) -> str:
        """
        Returns the string representation of this object.
        @return:        the string representation of this object
        """
        has_carry_on = "has carry on" if self.has_carry_on \
            else "doesn't have carry on"

        return "  " + self.name + " (" + self.ticket_number + ") " \
               + has_carry_on

    def get_zone(self) -> int:
        """
        Returns the boarding zone number of this passenger.
        @return:        boarding zone number of this passenger.
        """
        return int(self.ticket_number[0])
