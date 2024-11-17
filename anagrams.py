#!/usr/bin/env python3
"""Find anagrams of a given name."""

import load_dictionary

#word_list = load_dictionary.load("dictionary.txt") # short word list
word_list = load_dictionary.load("/usr/share/dict/american-english") # long word list

anagram_list = []

# input a SINGLE word or name to find its anagram(s)
name = input("Enter a name: ")

name = name.lower()
print(f"Using name = {name}\n")

# sort and find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# print out list of anagrams
if len(anagram_list) == 0:
    print("\nNo anagrams found\n")
else:
    print("Anagrams: ", *anagram_list, sep='\n')
