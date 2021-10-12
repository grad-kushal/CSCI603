
from aircraft import Aircraft
from passenger import Passenger
from zone import Zone

class Gate:

    __slots__ = "_zones", "_max_capacity"

    def __init__(self, max_capacity: int):

        self._max_capacity = max_capacity
        self._zones = []
        for i in range(4):
            self._zones.append(Zone(i + 1))

    def get_current_pax_count(self):
        """
        Returns the total number of people currently lined up in the gate.

        :return:        the total number of people currently lined up
                        in the gate
        """
        total_pax = 0
        for zone in self._zones:
            total_pax += zone.get_pax_count()

        return total_pax

    def add_pax(self, passenger: Passenger):

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

    def board_pax(self, aircraft: Aircraft):

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

    def is_empty(self):

        return self.get_current_pax_count() == 0
