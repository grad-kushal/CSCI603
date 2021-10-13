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


def test_pax_queue() -> None:
    """
    Tests the functionalities of the PaxQueue class

    @return:        None
    """
    test_pax_queue_is_empty()
    # TODO: implement these
    # test_pax_queue_enqueue()
    # test_pax_queue_dequeue()


def test_zone() -> None:
    """
    Tests the functionalities of the Zone class

    @return:        None
    """
    test_pax_queue_is_empty()
    test_zone_add_pax()
    test_zone_remove_pax()


def test_aircraft() -> None:
    """
    Tests the functionalities of the Aircraft class

    @return:        None
    """
    pass


def test_passenger() -> None:
    """
    Tests the functionalities of the Passenger class

    @return:        None
    """
    pass


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

        print("Passed all tests.")
    except AssertionError as e:
        print("Testing failed!")
        print(repr(e))


if __name__ == '__main__':
    main()
