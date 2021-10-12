"""
passenger.py
author: Kushal K, Arjun K
description: A passenger data type class for AiRIT assignment
"""


class Passenger:
    __slots__ = "name", "ticket_number", "has_carry_on"

    def __init__(self, name: str, ticket_number: str, has_carry_on=False):
        self.name = name
        self.ticket_number = ticket_number
        self.has_carry_on = has_carry_on

    def __str__(self):
        has_carry_on = "has carry on" if self.has_carry_on else "doesnt have carry on"
        return "  " + self.name + " (" + self.ticket_number + ") " + has_carry_on

    def get_zone(self) -> int:
        return int(self.ticket_number[0])


