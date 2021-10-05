
def binary_search(word_list: list[str], word: str) -> int:
    """
    Searches a word in the list of words using binary search.

    :param word_list:       list of words to search in
    :param word:            word to search
    :return:                if word is present in the list, index is returned;
                            else -1 is returned
    """
    if len(word_list) == 0:
        return False
    else:
        center = len(word_list) // 2
        if word_list[center] == word:
            return center
        else:
            result = binary_search(word_list[:center], word) \
                if word < word_list[center] \
                else binary_search(word_list[center + 1:], word)
            return result