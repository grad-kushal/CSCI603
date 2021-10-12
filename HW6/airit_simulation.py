"""
Filename:       airit_simulation.py
Description:    Assignment for Lab 6 of CSCI 603

                This program simulates operations of AiRIT

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""
import sys

from aircraft import Aircraft
from gate import Gate
from passenger import Passenger
from pax_queue import PaxQueue

def get_filename_from_args() -> str:
    """
    Parse the filename from the command line args.

    :return:        filename from args
    """
    if len(sys.argv) != 2:
        print("Error: Illegal command line arguments")
        print("Usage: python3 airit_simulation {filename}")
        exit(1)
    else:
        return sys.argv[1]


def get_positive_integer(prompt: str) -> int:
    while True:
        try:
            input_value = int(input(prompt))
            if input_value < 0:
                print("Invalid Input. A positive number is expected")
                continue
            else:
                break
        except ValueError:
            print("Invalid Input. An integer is expected")
            continue
    return input_value


def read_pax_from_file(filename: str) -> list[Passenger]:
    pax_list = []
    try:
        with open(filename) as f:

            lines = f.readlines()
            for line in lines:
                pax_details = line.split(",")

                pax_list.append(Passenger(pax_details[0],
                                          pax_details[1],
                                          eval(pax_details[2].strip())))
        return pax_list

    except FileNotFoundError as _:
        print("Filename not found %s" % filename)
        exit(1)


def get_user_input() -> tuple[int, int]:
    gate_capacity = get_positive_integer("Input gate capacity: ")
    aircraft_capacity = get_positive_integer("Input aircraft capacity")

    return gate_capacity, aircraft_capacity


def start_simulation(passengers: list[Passenger],
                     gate_capacity: int,
                     aircraft_capacity: int):

    print("Beginning simulation...")

    # create the gate object
    gate = Gate(gate_capacity)

    # create the aircraft object
    aircraft = Aircraft(aircraft_capacity)

    # create the line of passengers outside the gate
    line = PaxQueue()
    for passenger in passengers:
        line.enqueue(passenger)

    while not line.is_empty():
        print("Passengers are lining up at the gate...")

        while not line.is_empty():
            passenger = line.dequeue()
            print(passenger)
            if not gate.add_pax(passenger):
                print("The gate is full; remaining passengers must wait")
                break

        if line.is_empty():
            print("The last passenger is in line!")

        while not gate.is_empty():

            # board the passengers to the aircraft
            gate.board_pax(aircraft)

            # landing at the destination
            print("The aircraft has landed.")

            # deplane all the passengers from the aircraft
            aircraft.disembark()

    print("Simulation complete; all passengers are at their destination!")


def main() -> None:
    """
    Read file input and run the airit simulation
    :return:        None
    """

    # read the passenger filename from args
    filename = get_filename_from_args()

    # Start simulation
    passengers = read_pax_from_file(filename)

    gate_capacity, aircraft_capacity = get_user_input()

    start_simulation(passengers, gate_capacity, aircraft_capacity)


if __name__ == '__main__':
    main()

