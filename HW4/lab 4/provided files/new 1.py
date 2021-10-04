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