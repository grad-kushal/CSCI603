"""
Filename:       airit_tests.py
Description:    Assignment for Lab 6 of CSCI 603

                This module contains the unit tests for all the functionalities
                implemented as part of the AiRIT simulation program.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

import sys

import airit_simulation

from aircraft import Aircraft
from gate import Gate
from linked_node import LinkedNode
from passenger import Passenger
from pax_queue import PaxQueue
from pax_stack import PaxStack
from zone import Zone

# list of passenger objects to be used in the tests
TEST_PASSENGERS = [
    Passenger("PaxName", "1234", True),
    Passenger("PaxName", "2345", False),
    Passenger("PaxName", "3456", True),
    Passenger("PaxName", "4567", False),
]


def test_linked_node() -> None:
    """
    Test the implementation of the linked node.

    @return:        None
    """
    pax = TEST_PASSENGERS[0]

    node = LinkedNode(pax, None)
    assert str(node.passenger) == "  PaxName (1234) has carry on"
    assert node.link is None


def test_pax_stack_is_empty() -> None:
    """
    Test the PaxStack.is_empty method.

    @return:        None
    """
    stack = PaxStack()

    # before push
    assert stack.is_empty()

    pax = TEST_PASSENGERS[0]
    stack.push(pax)

    # after push
    assert not stack.is_empty()


def test_pax_stack_push() -> None:
    """
    Test the PaxStack.push method.

    @return:        None
    """
    stack = PaxStack()

    # before push
    assert stack.is_empty()

    pax = TEST_PASSENGERS[0]
    stack.push(pax)

    # after push
    assert not stack.is_empty()
    assert stack.peek() == pax


def test_pax_stack_pop() -> None:
    """
    Test the PaxStack.pop method.

    @return:        None
    """
    stack = PaxStack()
    assert stack.is_empty()

    pax = TEST_PASSENGERS[0]
    stack.push(pax)

    # before pop push
    assert not stack.is_empty()
    assert stack.peek() == pax

    pax_popped = stack.pop()

    # after pop
    assert pax_popped == pax
    assert stack.is_empty()


def test_pax_stack_peek() -> None:
    """
    Test the PaxStack.peek method.

    @return:        None
    """
    stack = PaxStack()

    # before push
    assert stack.is_empty()

    pax = TEST_PASSENGERS[0]
    stack.push(pax)

    # after push
    assert stack.peek() == pax


def test_pax_queue_is_empty() -> None:
    """
    Test the PaxQueue.is_empty method.

    @return:        None
    """
    queue = PaxQueue()

    # before enqueue
    assert queue.is_empty()

    pax = TEST_PASSENGERS[0]
    queue.enqueue(pax)

    # after enqueue
    assert not queue.is_empty()


def test_zone_add_pax() -> None:
    """
    Tests the functionalities of the Zone.add_pax method

    @return:        None
    """
    zone = Zone(1)

    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]

    # before adding pax
    assert zone.get_pax_count() == 0

    # add one pax
    zone.add_pax(pax1)

    # check the pax count
    assert zone.get_pax_count() == 1

    # add one more pax
    zone.add_pax(pax2)

    # check the pax count
    assert zone.get_pax_count() == 2


def test_zone_remove_pax() -> None:
    """
    Tests the functionalities of the Zone.remove_pax method

    @return:        None
    """
    zone = Zone(1)

    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]

    # before adding pax
    assert zone.get_pax_count() == 0

    # add pax
    zone.add_pax(pax1)
    zone.add_pax(pax2)

    # check pax count
    assert zone.get_pax_count() == 2

    # on removal, check whether FIFO order is followed
    # remove first pax
    assert zone.remove_pax() == pax1

    # remove second pax
    assert zone.remove_pax() == pax2


def test_zone_get_pax_count() -> None:
    """
    Tests the functionalities of the Zone.get_pax_count method

    @return:        None
    """

    zone = Zone(1)

    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]

    # before adding pax
    assert zone.get_pax_count() == 0

    # add pax
    zone.add_pax(pax1)
    zone.add_pax(pax2)

    # check pax count
    assert zone.get_pax_count() == 2


def test_gate_is_empty():
    """
    Tests the functionalities of the Gate.is_empty method

    @return:            None
    """

    gate = Gate(2)

    # before adding pax
    assert gate.is_empty()

    # add a pax
    gate.add_pax(TEST_PASSENGERS[0])

    # after insertion
    assert not gate.is_empty()


def test_gate_get_current_pax_count():
    """
    Tests the functionalities of the Gate.get_current_pax_count method

    @return:            None
    """

    gate = Gate(4)

    # before adding pax
    assert gate.is_empty()

    # add pax
    gate.add_pax(TEST_PASSENGERS[0])
    gate.add_pax(TEST_PASSENGERS[1])
    gate.add_pax(TEST_PASSENGERS[2])

    # after adding pax
    assert gate.get_current_pax_count() == 3


def test_gate_add_pax():
    """
    Tests the functionalities of the Gate.add_pax method

    @return:        None
    """

    gate = Gate(3)

    # before adding pax
    assert gate.is_empty()

    # add pax
    assert gate.add_pax(TEST_PASSENGERS[0])
    assert gate.add_pax(TEST_PASSENGERS[1])

    # after adding pax
    assert gate.get_current_pax_count() == 2
    assert not gate.is_empty()

    # check the passenger in the first boarding zone
    assert gate._zones[0].get_pax_count() == 1
    assert gate._zones[0]._pax_queue._front.passenger == TEST_PASSENGERS[0]

    # check the passenger in the second boarding zone
    assert gate._zones[1].get_pax_count() == 1
    assert gate._zones[1]._pax_queue._front.passenger == TEST_PASSENGERS[1]

    # adding the next pax should return false since the max limit will be
    # reached.
    assert not gate.add_pax(TEST_PASSENGERS[2])

    # check the boarding zone
    assert gate._zones[2].get_pax_count() == 1
    assert gate._zones[2]._pax_queue._front.passenger == TEST_PASSENGERS[2]

    # But this passenger should nonetheless be added to the gate
    assert gate.get_current_pax_count() == 3

    # subsequent addition should return false
    assert not gate.add_pax(TEST_PASSENGERS[3])

    # AND this passenger shouldn't be added to the gate
    assert gate.get_current_pax_count() == 3


def test_gate_board():
    """
    Tests the functionalities of the Gate.add_pax method

    @return:
    """

    aircraft = Aircraft(2)

    gate = Gate(4)

    # add pax
    gate.add_pax(TEST_PASSENGERS[0])
    gate.add_pax(TEST_PASSENGERS[1])
    gate.add_pax(TEST_PASSENGERS[2])
    gate.add_pax(TEST_PASSENGERS[3])

    # board pax to plane
    gate.board_pax(aircraft)

    # 2 should be boarded, 2 should remain back in the gate
    assert aircraft.is_full()
    assert gate.get_current_pax_count() == 2

    # check the pax in the boarding zones
    assert gate._zones[0].get_pax_count() == 1
    assert gate._zones[0]._pax_queue._front.passenger == TEST_PASSENGERS[0]

    assert gate._zones[1].get_pax_count() == 1
    assert gate._zones[1]._pax_queue._front.passenger == TEST_PASSENGERS[1]

    assert gate._zones[2].get_pax_count() == 0

    assert gate._zones[3].get_pax_count() == 0

    # create a new aircraft
    aircraft = Aircraft(2)

    # board pax
    gate.board_pax(aircraft)

    # all pax boarded, gate should be empty
    assert aircraft.is_full()
    assert gate.is_empty()


def test_pax_stack() -> None:
    """
    Tests the functionalities of the PaxStack class

    @return:        None
    """
    test_pax_stack_is_empty()
    test_pax_stack_push()
    test_pax_stack_pop()
    test_pax_stack_peek()


def test_pax_queue_enqueue() -> None:
    """
    Test the PaxQueue.enqueue method.

    @return:        None
    """
    queue = PaxQueue()
    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]

    # before enqueue
    assert queue.is_empty()
    queue.enqueue(pax1)
    # after enqueue
    assert not queue.is_empty()
    assert queue._front == queue._back
    assert queue._front.passenger == pax1

    queue.enqueue(pax2)

    # after 2nd enqueue
    assert not queue.is_empty()
    assert queue._back.passenger == pax2
    assert queue._front.passenger == pax1


def test_pax_queue_dequeue() -> None:
    """
    Test the PaxQueue.enqueue method.

    @return:        None
    """
    queue = PaxQueue()
    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]

    assert queue.is_empty()

    queue.enqueue(pax1)
    queue.enqueue(pax2)

    # before dequeue
    assert not queue.is_empty()

    dq_pax = queue.dequeue()

    # after dequeue
    assert dq_pax == pax1
    assert queue._front.passenger == pax2

    dq_pax = queue.dequeue()

    # after 2nd dequeue
    assert dq_pax == pax2
    assert queue._front is None
    assert queue._back is None
    assert queue.is_empty()


def test_airit_simulation_get_filename_from_args() -> None:
    """
    Test the functionality of the airit_simulation.get_filename_from_args

    @return:    None
    """

    # mock sys.argv
    sys.argv = ["module.py", "filename.txt"]

    actual = airit_simulation.get_filename_from_args()
    expected = "filename.txt"

    assert actual == expected


def test_airit_simulation_read_pax_from_file():
    """
    Test the functionality of the airit_simulation.read_pax_from_file

    @return:    None
    """

    filename = "passengers_very_small.txt"

    passengers = airit_simulation.read_pax_from_file(filename)

    # assert the number of objects created
    assert len(passengers) == 10

    # assert all the objects are of type Passenger
    for pax in passengers:
        assert isinstance(pax, Passenger)


def test_aircraft_is_empty() -> None:
    """
    Tests the Aircraft.is_empty()

    @return:        None
    """

    pax = TEST_PASSENGERS[0]
    aircraft = Aircraft(5)

    # before boarding
    assert aircraft.is_empty()

    aircraft.board(pax)

    # after boarding
    assert not aircraft.is_empty()


def test_aircraft_is_full() -> None:
    """
    Tests the Aircraft.is_full()

    @return:        None
    """

    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]
    aircraft = Aircraft(2)

    # before boarding
    assert not aircraft.is_full()

    aircraft.board(pax1)
    aircraft.board(pax2)

    # after boarding
    assert aircraft.is_full()


def test_aircraft_deplane() -> None:
    """
    Tests the Aircraft.deplane()

    @return:        None
    """

    aircraft = Aircraft(2)

    assert aircraft.is_empty()

    dp_pax = aircraft.deplane()

    assert dp_pax is None

    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]

    aircraft.board(pax1)
    aircraft.board(pax2)

    assert aircraft.is_full()

    pax_count = aircraft._current_pax
    dp_pax = aircraft.deplane()

    assert aircraft._current_pax == pax_count - 1
    assert dp_pax == TEST_PASSENGERS[1]

    pax_count = aircraft._current_pax
    dp_pax = aircraft.deplane()

    assert aircraft._current_pax == pax_count - 1
    assert dp_pax == TEST_PASSENGERS[0]


def test_aircraft_disembark() -> None:
    """
    Tests the Aircraft.disembark()

    @return:        None
    """
    aircraft = Aircraft(2)

    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]

    aircraft.board(pax1)
    aircraft.board(pax2)

    # before disembark
    assert not aircraft.is_empty()

    aircraft.disembark()

    # after disembark
    assert aircraft.is_empty()


def test_aircraft_board() -> None:
    """
    Tests the Aircraft.board()

    @return:        None
    """

    aircraft = Aircraft(2)

    pax1 = TEST_PASSENGERS[0]
    pax2 = TEST_PASSENGERS[1]
    pax3 = TEST_PASSENGERS[2]

    # before board
    assert aircraft.is_empty()

    pax_count = aircraft._current_pax
    result = aircraft.board(pax1)

    # after board
    assert not aircraft.is_empty()
    assert aircraft._current_pax == pax_count + 1
    assert aircraft._pax_with_carry_on.peek() == pax1
    assert result is None

    pax_count = aircraft._current_pax
    result = aircraft.board(pax2)

    # after 2nd board
    assert aircraft.is_full()
    assert aircraft._current_pax == pax_count + 1
    assert aircraft._pax_without_carry_on.peek() == pax2
    assert result is None

    pax_count = aircraft._current_pax
    result = aircraft.board(pax3)

    assert aircraft.is_full()
    assert aircraft._current_pax == pax_count
    assert result is False


def test_passenger_get_zone() -> None:
    pax = TEST_PASSENGERS[0]
    zone = pax.get_zone()

    assert zone == 1


def test_pax_queue() -> None:
    """
    Tests the functionalities of the PaxQueue class

    @return:        None
    """
    test_pax_queue_is_empty()
    test_pax_queue_enqueue()
    test_pax_queue_dequeue()


def test_zone() -> None:
    """
    Tests the functionalities of the Zone class

    @return:        None
    """
    test_zone_get_pax_count()
    test_zone_add_pax()
    test_zone_remove_pax()


def test_aircraft() -> None:
    """
    Tests the functionalities of the Aircraft class

    @return:        None
    """
    test_aircraft_is_empty()
    test_aircraft_is_full()
    test_aircraft_deplane()
    test_aircraft_board()
    test_aircraft_disembark()


def test_passenger() -> None:
    """
    Tests the functionalities of the Passenger class

    @return:        None
    """
    test_passenger_get_zone()


def test_gate() -> None:
    """
    Tests the functionalities of the Gate class

    @return:        None
    """
    test_gate_is_empty()
    test_gate_get_current_pax_count()
    test_gate_add_pax()
    test_gate_board()


def test_airit_simulation() -> None:
    """
    Tests the functionalities of the airit_simulation module

    @return:        None
    """
    test_airit_simulation_get_filename_from_args()
    test_airit_simulation_read_pax_from_file()


def main() -> None:
    """
    Run all the tests

    @return:        None
    """

    try:
        # test the LinkedNode class
        test_linked_node()

        # test the PaxStack class
        test_pax_stack()

        # test the zone class
        test_zone()

        # test the PaxQueue class
        test_pax_queue()

        # test the passenger class
        test_passenger()

        # test the Aircraft class
        test_aircraft()

        # test the gate class
        test_gate()

        # test airit_simulation
        test_airit_simulation()

        print("*" * 80)
        print("Passed all tests.")
        print("*" * 80)
    except AssertionError as e:
        print("x" * 80)
        print("Testing failed!")
        print("x" * 80)
        raise e


if __name__ == '__main__':
    main()
