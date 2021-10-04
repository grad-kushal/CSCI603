"""
Filename:       spellfixer.py
Description:    Assignment for Lab 4 of CSCI 603

                This program reads sentences from the user as input, performs
                a spellcheck on each word, and outputs the correct line if
                mistakes were found.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

import re
import sys

from ritcs.mutable_str import mutable_str


def fix_qwerty_error(raw_word: str, legal_words, qwerty_adjacent) -> str:
    """

    :param raw_word:
    :param legal_words:
    :param qwerty_adjacent:
    :return:
    """

    # change to a mutable string
    word = mutable_str(raw_word)

    for letter in word:
        try:
            adj_letters = qwerty_adjacent[letter]

        except KeyError:
            pass

def fix_transpose_error(raw_word: str, legal_words: set[str]) -> str:
    """

    :param raw_word:            word to spellcheck
    :param legal_words:         set of legal words
    :return:
    """
    
    # change to a mutable string
    word = mutable_str(raw_word)
    for i in range(0, len(word)-1):
        word[i], word[i+1] = word[i+1] , word[i]
        if str(word) in legal_words:
            return str(word)
        word = mutable_str(raw_word)
    

def do_spellcheck(raw_word, legal_words, qwerty_adjacent) -> str:
    """
    Separates the word from the leading and trailing whitespaces
    and punctuations.

    :param raw_word:            word to preprocess
    :param legal_words:         set of legal words
    :param qwerty_adjacent:     dict containing information about adjacent
                                keys in a QWERTY keyboard
    :return:                    tuple of the following format:
                                (leading punctuations/whitespaces,
                                word, trailing punctuations)
    """

    punctuation_regex = re.compile(r'[.,!;:@#$%^&\*]')

    start_punctuation = ""  # punctuation at the start of the word, if any
    end_punctuation = ""  # punctuation at the end of the word, if any

    # strip off punctuations at start and end (if any)
    if punctuation_regex.match(raw_word[0]):
        raw_word = raw_word[1:]
        start_punctuation = raw_word[0]

    if punctuation_regex.match(raw_word[-1]):
        raw_word = raw_word[:-1]
        end_punctuation = raw_word[-1]

    # check if this word is in the set of legal words
    if raw_word in legal_words:
        return start_punctuation + raw_word + end_punctuation

    corrected_word = fix_qwerty_error(raw_word, legal_words, qwerty_adjacent)

    if corrected_word != raw_word:  # some correction was done
        return start_punctuation + raw_word + end_punctuation

    corrected_word = fix_transpose_error(raw_word, legal_words)
    
    if corrected_word != raw_word:  # some correction was done
        return start_punctuation + raw_word + end_punctuation

def process_line(line: str, legal_words: set[str], 
                 qwerty_adjacent: dict[str, set[str]]) -> str:
    """
    Reconstruct the line by doing all the spellchecks.

    :param line:                line to process
    :param legal_words:         set of legal words
    :param qwerty_adjacent:     dict containing information about adjacent
                                keys in a QWERTY keyboard
    :return:                    line with spellchecked words
    """

    # split the word on whitespaces
    line_split = line.split(" ")

    reconstructed_line = mutable_str("")
    for raw_word in line_split:
        if raw_word:
            reconstructed_line.append(
                do_spellcheck(raw_word, legal_words, qwerty_adjacent)
            )

        reconstructed_line += " "

    return str(reconstructed_line)


def get_filenames_from_args() -> tuple[str, str]:
    """
    Get the paths of the files containing the words and qwerty key distribution
    from the arguments passed to the program.

    :return:        tuple with file paths of words and qwerty keyboard
                    distribution (in that order)
    """
    args = sys.argv

    try:
        words_filename = args[1]
        qwerty_filename = args[2]

        return words_filename, qwerty_filename
    except IndexError:
        msg = "Both file paths were not provided.\n"\
              + "Run the program using the following command format:\n"\
              + "python3 spellfixer.py <words-filepath> <keyboards-filepath>"
        print(msg)
        exit(1)


def read_adjacent_keys_info(adj_keys_filepath: str) -> dict[str, set[str]]:
    """
    Read the contents of the file containing the information about adjacent
    keys.

    :param adj_keys_filepath:           path of the file containing the
                                        QWERTY key distribution
    :return:                            adjacent keys information as a dict
    """

    # read lines from the qwerty keys distribution file
    with open(adj_keys_filepath) as f:
        qwerty_key_distribution = f.readlines()

    # populate the qwerty adjacent keys information to a dict
    qwerty_adjacent = dict()
    for line in qwerty_key_distribution:
        key = line[0]  # get the key whose data is to be added

        # split the subsequent line on " " to get the adjacent keys
        adj_keys_split = line[2:].split(" ")

        # the set of keys adjacent to 'key'
        adjacent_keys = set()
        for adj_key in adj_keys_split:
            adjacent_keys.add(adj_key.strip())

        qwerty_adjacent[key] = adjacent_keys
    return qwerty_adjacent


def read_legal_words_from_file(words_filepath: str) -> set[str]:
    """
    Read the contents of the file containing the legal words, process it to
    remove the trailing newline character, and return the legal words as a set.

    :param words_filepath:                  path of the file containing the
                                            legal words
    :return:                                set of legal words
    """
    # read the legal words from the file
    with open(words_filepath) as f:
        lines = f.readlines()

    legal_words = set()
    for line in lines:
        legal_words.add(line.strip().lower())

    return legal_words


def read_data_from_files(words_filepath: str,
                         qwerty_distribution_filepath: str
                         ) -> (set[str], dict[str], list[str]):
    """
    Read the contents of filenames provided as argument. For words, the set
    of legal words are returned. For QWERTY key distribution, a dict where
    keys are letter in the keyboard and the the corresponding values
    are the keys adjacent to that letter.

    :param words_filepath:                  path of the file containing the
                                            legal words
    :param qwerty_distribution_filepath:    path of the file containing the
                                            QWERTY key distribution
    :return:                                tuple containing the set of
                                            legal words, and the QWERTY
                                            adjacent keys information
    """

    try:
        # get the set of legal words
        legal_words = read_legal_words_from_file(words_filepath)

        # get the QWERTY adjacent keys information
        qwerty_adjacent = read_adjacent_keys_info(qwerty_distribution_filepath)

        return legal_words, qwerty_adjacent

    except FileNotFoundError as fnf:
        print("File not found: " + str(fnf))
        exit(1)


def start_spellcheck(legal_words: set[str],
                     qwerty_adjacent: dict[str, set[str]]) -> None:
    """
    Gets input line from the user, and performs spellcheck to output
    corrected line (if applicable)

    :param legal_words:         set of legal words
    :param qwerty_adjacent:     dict with information about all keys adjacent to
                                a key in the QWERTY keyboard
    :return:                    None
    """

    # receive input from the user
    line = input("> ")

    while line != "!*!":
        corrected_line = process_line(line, legal_words, qwerty_adjacent)
        print(corrected_line)
        line = input("> ")


def main():
    words_filepath, qwerty_filepath = get_filenames_from_args()
    legal_words, qwerty_adjacent = read_data_from_files(words_filepath,
                                                        qwerty_filepath)

    start_spellcheck(legal_words, qwerty_adjacent)

    #
    #
    # from pprint import pprint
    # pprint(qwerty_adjacent)
    # #m start_spellcheck(legal_words, qwerty_adjacent)
    #
    # x = set()
    #
    # for y in qwerty_adjacent:
    #     x = x.union(qwerty_adjacent[y])
    #
    # print(x)


if __name__ == "__main__":
    main()
