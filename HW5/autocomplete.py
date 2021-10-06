"""
Filename:       autocomplete.py
Description:    Assignment for Lab 5 of CSCI 603

                This program prompts the user to enter a prefix and suggests
                auto-complete words starting with the prefix.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

import sys

from bsearch import index_of_first
from sort import merge_sort


def get_filename_from_args() -> str:
    """
    Parse the filename from the command line args.

    :return:        filename from args
    """

    args = sys.argv
    if len(args) < 2:
        print("Error: Filename not provided")
        print("Usage: python3 auto_complete filename")
        exit(1)

    return args[1]


def read_words_from_file(filepath: str) -> list[str]:
    """
    Build a list of words from the input file.

    :param filepath:    path of the file to read from
    :return:           list of words read from the file
    """

    try:
        with open(filepath) as f:

            # strip '\n' from the end of each word
            words = [word.strip().lower() for word in f.readlines()]

        return words
    except FileNotFoundError as _:
        print("Filename %s was not found" % filepath)
        exit(1)


def get_autocomplete_suggestions(prefix: str, 
                                 sorted_words: list[str]) -> list[str]:
    """
    Using the prefix entered, generate a list of auto-complete word suggestions.

    :param prefix:          word prefix
    :param sorted_words:    list of sorted words
    :return:                list of auto-complete suggestions
    """

    start_index = index_of_first(sorted_words, prefix)

    if start_index == -1:

        # no words with the prefix exists
        return []

    # index used to iterate over the list of sorted words
    current_index = start_index
    suggestions = []

    # create a list of all words starting with the prefix
    while current_index < len(sorted_words) \
            and sorted_words[current_index].startswith(prefix):
        suggestions.append(sorted_words[current_index])
        current_index += 1

    return suggestions


def run(sorted_words) -> None:
    """
    Read q prefix as input from the user and display auto-complete
    suggestions.

    :param sorted_words:    list of sorted words
    :return:                prefix read from the user
    """

    print("Welcome to the auto-complete program!\n")

    # read prefix from user
    prefix = input("Enter the prefix: ")

    # list of auto-complete suggestions; default is the list of sorted words
    previous_results = sorted_words

    # index of the list containing previous search results
    index = 0

    while prefix != "<QUIT>":

        if prefix == "" and previous_results:
            print(previous_results[index])
            index = (index + 1) % len(previous_results)

        if prefix:

            # get the auto-complete suggestions
            suggestions = get_autocomplete_suggestions(
                prefix.lower(), sorted_words
            )

            if suggestions:

                # print the first suggestion
                print(suggestions[0])

            else:
                print("**No suggestions**")

            # store the suggestions for this prefix
            previous_results = suggestions

            if previous_results:

                # cycle through suggestions if empty prefix is entered next
                index = (index + 1) % len(previous_results)

        # read the next prefix from user
        prefix = input("Enter the prefix: ")

    print("Goodbye!")


def main() -> None:
    """
    Prompts the user to enter word prefixes to search for and displays
    the auto-complete word suggestions.

    :return:        None
    """

    # read the filename from args
    filename = get_filename_from_args()

    # read the list of unsorted words
    unsorted_words = read_words_from_file(filename)

    # sort the words
    sorted_words = merge_sort(unsorted_words)

    # print the sorted words
    print("The sorted words are: ")
    for word in sorted_words:
        print(word)

    # verification of sort
    unsorted_words.sort()
    for i in range(len(sorted_words)):
        assert sorted_words[i] == unsorted_words[i]

    # run the autocorrect suggestion program
    run(sorted_words)


if __name__ == '__main__':
    main()
