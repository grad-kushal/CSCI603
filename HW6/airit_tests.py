"""
Filename:       airit_tests.py
Description:    Assignment for Lab 6 of CSCI 603

                This module contains the unit tests for all the functionalities
                implemented as part of the AiRIT simulation program.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""
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
    test_pax_queue_is_empty()
    test_zone_add_pax()
    test_zone_remove_pax()


def test_aircraft_is_empty() -> None:

    pax = TEST_PASSENGERS[0]
    aircraft = Aircraft(5)

    # before boarding
    assert aircraft.is_empty()

    aircraft.board(pax)

    # after boarding
    assert not aircraft.is_empty()


def test_aircraft_is_full() -> None:

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


def test_passenger_get_zone() -> None:
    pax = TEST_PASSENGERS[0]
    zone = pax.get_zone()

    assert zone == 1


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
    pass


def test_airit_simulation() -> None:
    """
    Tests the functionalities of the airit_simulation module

    @return:        None
    """
    pass


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

        print("Passed all tests.")
    except AssertionError as e:
        print("Testing failed!")
        print(repr(e))


if __name__ == '__main__':
    main()
