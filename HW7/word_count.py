"""
description: Word Count Program for CSCI 141/603
file: word_count.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: bks@cs.rit.edu ben k steele
author: jsb@cs.rit.edu Jeremy Brown
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: mjc@cs.rit.edu Maria Cepeda
"""

from hashmap import HashMap
from hash_functions import hash_function_naive, hash_function_improved


def word_count(hTable, filename):
    """
        Record the frequency of all words in the named file in the hashtable.
        word_count : HashTable String -> HashTable
    """

    # Read the words of the text file into the word count table.
    with open(filename) as fd:
        for line in fd:
            for word in line.split():
                # using a regular expression argument to strip(),
                # strip out punctuation and convert token to lower-case.
                word = word.strip(",.\"\';:-!?").lower()
                if hTable.contains(word):
                    count = hTable.get(word)
                    hTable.add(word, count + 1)
                else:
                    hTable.add(word, 1)

    return hTable


def printSummary(theTable):
    """
    printSummary prints a summary of information about the hash table contents.
    printSummary : HashTable -> NoneType
    """

    # Display the entire table!
    # Find the most common word in the text file.
    total = 0
    maxWord = ""
    maxCount = 0
    for key, thisCount in theTable:
        total += thisCount
        if thisCount > maxCount:
            maxCount = thisCount
            maxWord = key

    print("Unique words:", theTable.size)
    print("Total words:", total)
    print('"' + maxWord + "\" appeared ", str(maxCount),
          " times, more than any other word.")


def printTable(hTable):
    """
        Print the contents of the given hash table.
        Each key/value pair is displayed in parentheses, tuple-style.
        All pairs appear on a single line.
        printTable : HashTable -> NoneType
    """
    print("Word Count Data ---------------")
    ltext = 0
    for key, value in hTable:
        # print( "(" + key + "," + str( get( hTable, key ) ) + ")", end=" " )
        txt = "(" + key + "," + str(value) + ")"
        ltext += len(txt)
        if ltext > 51:
            print(txt)
            ltext = 0
        else:
            print(txt, end=" ")
    print()


def hash_function(val):
    """
    hash_function: K NatNum -> NatNum
    Compute a hash of the val string that is in [0 ... n).
    """
    return hash(val)


def printMenu(wordTable):
    while True:
        print("Commands: k[ey] <word> f[ind] <word> q[uit] ? ", end=" ")
        response = input(":- ")  # the displayed prompt
        query = response.split()

        if len(response) == 0 or not response[0] in "fkq":
            print(response + " invalid. Please enter a command and a word.")
            response = ""
            continue

        if query[0] == "k":
            print("( " + query[1] + " in text ) is " \
                  + str(wordTable.contains(query[1])) + ".")

        if query[0] == "f":
            if wordTable.contains(query[1]):
                print(query[1] + " appears " \
                      + str(wordTable.get(query[1])) + " times.")
            else:
                print(query[1] + " is not in the text.")

        if query[0] == "q":
            break
    #
    answer = input("Do you want to see the entire table?(y/n) ")
    if answer != "y":
        return
    printTable(wordTable)


def main():
    capacity = int(input("Enter capacity (-1 for default): "))
    if capacity < 0:
        hTable_naive = HashMap(hash_function_naive)
        hTable_improved = HashMap(hash_function_improved)
    else:
        hTable_naive = HashMap(hash_function_naive, capacity)
        hTable_improved = HashMap(hash_function_improved, capacity)
    filename = input("Enter filename: ")

    wordTable_naive = word_count(hTable_naive, filename)
    wordTable_improved = word_count(hTable_improved, filename)
    print("Summary for wordTable naive: ")
    printSummary(wordTable_naive)

    print("Summary for wordTable imporved: ")
    printSummary(wordTable_improved)

    print("Menu for table (naive)")
    printMenu(wordTable_naive)

    print("Menu for table (improved)")
    printMenu(wordTable_improved)

    print("Imbalance value (naive): ", wordTable_naive.imbalance())
    print("Imbalance value (improved): ", wordTable_improved.imbalance())

# run the main program
if __name__ == '__main__':
    main()
