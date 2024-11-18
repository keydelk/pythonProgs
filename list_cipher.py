#!/usr/bin/env python3
"""Hides plaintext message as a null cipher in a list."""
import string
import load_dictionary

input_message = "meet at dawn"

# strip whitespace and non-alphabetic characters
message = ''
for char in input_message:
    if char in string.ascii_letters:
        message += char
print(message, "\n")

# open dictionary file
word_list = load_dictionary.load('groceries.txt')

# build list of words for cipher
cipher_list = []
for letter in message:
    for word in word_list:
        if word[2].lower() == letter.lower() and word not in cipher_list:
            cipher_list.append(word)
            break

if len(cipher_list) != len(message):
    print("Word list too small, try another")
else:
    print("Grocery List:\n", *cipher_list, sep="\n")
