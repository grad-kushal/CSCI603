"""
Filename:       bsearch.py
Description:    Assignment for Lab 5 of CSCI 603

                This module contains the method to search for the first
                occurrence of the string with a specified prefix.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""


def _binary_search(word_list: list[str],
                   prefix: str, start: int, end: int) -> int:
    """
    Recursively searches for the index of the first occurrence of the
    word with the given index.

    :param word_list:       list of words to search in
    :param prefix:          prefix to search fort the search from
    :param start:           index to star the search from
    :param end:             index to end the search in
    :return:                if a word is present in the list, index of the
                            first occurrence is returned; else -1 is returned
    """
    if start > end:
        return -1

    # calculate the mid index
    mid = (start + end) // 2

    if (not word_list[mid].startswith(prefix)) and word_list[mid] > prefix:
        return _binary_search(word_list, prefix, start, mid - 1)

    if (not word_list[mid].startswith(prefix)) and word_list[mid] < prefix:
        return _binary_search(word_list, prefix, mid + 1, end)

    if word_list[mid].startswith(prefix):

        # check if there exists a word in the left half that starts with the
        # prefix
        smaller_index = _binary_search(word_list, prefix, start, mid - 1)

        if smaller_index >= 0:
            return smaller_index

        return mid


def index_of_first(word_list: list[str], prefix: str) -> int:
    """
    Return the index of the first occurrence of the word with the given index.

    :param word_list:       list of words to search in
    :param prefix:          prefix to search fort the search from
    :return:                if a word is present in the list, index of the
                            first occurrence is returned; else -1 is returned
    """
    return _binary_search(word_list, prefix, 0, len(word_list) - 1)
