
def merge_sort(word_list: list[str]) -> list[str]:
    """
    Sort the list of word lexicographically using merge sort.

    :param word_list:       list of words tp be sorted
    :return:                sorted list of words
    """
    if len(word_list) <= 1:
        return word_list
    else:
        mid = len(word_list) // 2
        lefthalf = merge_sort(word_list[:mid])
        righthalf = merge_sort(word_list[mid:])

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                word_list[k] = lefthalf[i]
                i += 1
            else:
                word_list[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            word_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            word_list[k] = righthalf[j]
            j = j + 1
            k = k + 1
        return word_list
