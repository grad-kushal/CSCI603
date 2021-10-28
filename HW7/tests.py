"""
file: tests.py
description: Verify the chained hash map class implementation
"""

__author__ = ["Arjun Kozhissery (ak8913)", "Kushal Kale (ksk7657)"]

from hashmap import HashMap


def print_map(a_map):
    for word, counter in a_map:  # uses the iter method
        print(word, counter, end=" ")
    print()


def test0():
    table = HashMap(initial_num_buckets=10)
    table.add("to", 1)
    table.add("do", 1)
    table.add("is", 1)
    table.add("to", 2)
    table.add("be", 1)

    print_map(table)

    print("'to' in table?", table.contains("to"))
    print("'to' appears", table.get("to"), "times")
    table.remove("to")
    print("'to' in table?", table.contains("to"))

    print_map(table)


def test_expand_table() -> None:
    """
    Test whether the hash table is expanding when the load limit of the table
    is reached.
    @return:        None
    """
    print("Running test case for expanding hash table")
    table = HashMap(initial_num_buckets=5, load_limit=0.75)
    assert table.load == 0.0  # initial load is 0

    table.add("one", 1)
    table.add("two", 2)
    table.add("three", 3)
    assert table.load == 3 / 5

    # adding this element should cause the load factor to be surpassed
    table.add("four", 4)

    # assert values
    assert table.size == 4
    assert table.capacity == 10  # capacity should double


def test_expand_shrink() -> None:
    """
    Test whether the hash table is shrinking when the load limit of the table
    is reached.

    @return:        None
    """
    print("Running test case for shrinking hash table")
    table = HashMap(initial_num_buckets=6, load_limit=0.5)
    assert table.load == 0.0  # initial load is 0

    table.add("one", 1)
    table.add("two", 2)
    table.add("three", 3)

    assert table.load == 3 / 6

    # removing this element should cause the table to shrink
    table.remove("three")

    # assert values
    assert table.size == 2
    assert table.capacity == 3  # capacity should halved


def test_iter() -> None:
    """
    Test iterator.

    @return:        None
    """
    print("Running test case for iterator")
    table = HashMap(initial_num_buckets=5)

    table.add("one", 1)
    table.add("two", 2)
    table.add("three", 3)
    table.add("four", 4)

    expected_keys = ["one", "two", "three", "four"]
    expected_values = [1, 2, 3, 4]

    i = 0
    for key, value in table:
        # check if the key is present in the list of expected keys
        assert key in expected_keys

        # remove the key from the list (to ensure all values are uniquely
        # checked)
        expected_keys.remove(key)

        # check if the value is present in the list of expected values
        assert value in expected_values

        # remove the value from the list (to ensure all values are uniquely
        # checked)
        expected_values.remove(value)
        i += 1

    assert i == 4  # corresponds to 4 entries


if __name__ == '__main__':
    test0()
    test_expand_table()
    test_expand_shrink()
    test_iter()
    print("Testing complete")

