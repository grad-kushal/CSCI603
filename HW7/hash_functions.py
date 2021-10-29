from typing import Hashable


def hash_function_naive(key: Hashable) -> int:
    """
    Hash function that adds up the digits associated with the letter.

    @param key:         key to be hashed
    @return:            hash value
    """
    hash_value = 0
    for letter in key:
        hash_value += ord(letter)

    return hash_value


def hash_function_improved(key: Hashable) -> int:
    """
    Hash function that adds up the scaled digits associated with the letter.
    @param key:         key to be hashed
    @return:            hash value
    """
    hash_value = 0
    scale_factor = 1
    for letter in key:
        hash_value += ord(letter) * scale_factor
        scale_factor *= 31

    return hash_value
