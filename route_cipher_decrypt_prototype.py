#!/usr/bin/env python3
"""Decrypt a path through a Union Route Cipher

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either the top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at the bottom and read up.
Positive column numbers mean start at the top and read down.

Example below is for a 4x4 matrix with key -1 2 -3 4
Note "O" is not allowed.
Arrows show the encryption rout: for negative key values, read UP.

 1 2 3 4




"""
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# split elements into words
cipherlist = list(ciphertext.split())

# initialize variables
COLS = 4
ROWS = 5
key = '-1 2 -3 4'  # neg number means read UP column vs. DOWN
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

# turn key into list of integers
key_int = [int(i) for i in key.split()]

# turn columns into items in list of lists:
for k in key_int:
    if k < 0:  # read column from bottom to top
        col_items = cipherlist[start:stop]
    else:  # read column from top to bottom
        col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print(f"ciphertext = {ciphertext}")
print("translation_matrix = ", *translation_matrix, sep="\n")
print(f"key length = {len(key_int)}")

# decrypt by looping thouth nested lists popping off the last items
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print(f"plaintext = {plaintext}")
