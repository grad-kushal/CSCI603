from bsearch import search
from sort import sort


previously_search_results = []  # list of auto-complete suggestions
all_words = []  # list of the words to look up suggestions from


def get_prefix_from_user() -> str:
    """
    Read q prefix as input from the user.

    :return:            prefix read from the user
    """
    pass


def read_words_from_file(filepath: str) -> list[str]:
    """
    Build a list of words from the input file.

    :param filepath:    path of the file to read from
    :return:           list of words read from the file
    """
    pass


def get_autocomplete_suggestions(prefix: str) -> list[str]:
    """
    Using the prefix entered, generate a list of auto-complete word suggestions.

    :param prefix:          word prefix
    :return:                list of auto-complete suggestions
    """
    pass


def run() -> None:
    """
    Read prefixes from the user and suggest auto-complete words.

    :return:          None
    """


def main() -> None:
    """
    Prompts the user to enter word prefixes to search for and displays
    the auto-complete word suggestions.

    :return:        None
    """
    pass


if __name__ == '__main__':
    main()
