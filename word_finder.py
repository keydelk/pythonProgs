#!/usr/bin/env python3

# This word finder program returns a list of all dictionary words
# that can be made with the letters given. By default it requires the
# first letter and needs a minimum of 4 letters.
# This can be run interactively or with command line arguments. It can
# also be imported as a module into other programs.

import sys
import argparse
import load_dictionary

def main():
    """Run Program from command line."""
    # read command line arguments
    parser = argparse.ArgumentParser(description='This program finds words consisting of only the given letters')
    parser.add_argument('-l', '--letters', type=str, help='Letters allowed', default='')
    parser.add_argument('-d', '--dictionary', type=str, help='file path of the dictionary to use',
                        default="/usr/share/dict/american-english")
    args = parser.parse_args()
    letters = args.letters
    # prompt user for letters if none provided:
    if not letters:
        letters = input("Enter letters, required letter first: ")
    # make sure everything is lower case
    letters = letters.lower()
    # generate the list of  found words
    found_words = find_words(letters, dictionary=args.dictionary)
    # print out list of found words
    if len(found_words) == 0:
        print("\nNo words found.\n")
    else:
        print("Words found: ", *found_words, sep='\n')
    return 0


def find_words(letters, dictionary="/usr/share/dict/american-english"):
    """Returns all words >= 4 characters that can be made with the given letters in a list."""
    word_list = load_dictionary.load(dictionary)
    found_words = []
    # loop through word list to find words that can be made with letters
    # to make this like the spelling bee game, the first letter in letters must
    # be in the word, and the word must be at least 4 letters
    for word in word_list:
        if len(word) < 4 or letters[0] not in word:
            continue
        for char in word:
            if char not in letters:
                break
        else:
            found_words.append(word)
    return found_words

if __name__ == '__main__':
    sys.exit(main())
