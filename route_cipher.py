#!/usr/bin/env python3
"""Encrypt or decrypt a Union Route Cipher

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either the top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at the bottom and read up.
Positive column numbers mean start at the top and read down.

Example below is for a 4x4 matrix with key -1 2 -3 4
Note "O" is not allowed.
Arrows show the encryption rout: for negative key values, read UP.

 1 2 3 4
┌─┬─┬─┬─┐
│↑│↓│↑│↓│ Message is written
├─┼─┼─┼─┤
│↑│↓│↑│↓│ Across each row
├─┼─┼─┼─┤
│↑│↓│↑│↓│ In this manner
├─┼─┼─┼─┤
│↑│↓│↑│↓│ Last Row is filled with dummy words
└─┴─┴─┴─┘
start  end

Required inputs - a text message and key string
"""
import sys


def main():
    """Run program from command line."""
    while True:
        encrypt_or_decrypt = input("[E]ncrypt or [D]ecrypt? ").upper()
        if encrypt_or_decrypt[0] == 'E':
            plaintext = input("Enter plaintext (and padding) to encrypt: ")
            key = input("Enter encryption key (e.g. -1 2 -3 4): ")
            if len(plaintext.split()) % len(key.split()) != 0:
                print("Number of words must be a multiple of the length of the key.")
                continue
            ciphertext = encrypt(plaintext, key)
            print(f"Ciphertext: {ciphertext}")
        elif encrypt_or_decrypt[0] == 'D':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter encryption key (e.g. -1 2 -3 4): ")
            if len(ciphertext.split()) % len(key.split()) != 0:
                print("Number of words must be a multiple of the length of the key.")
                continue
            plaintext = decrypt(ciphertext, key)
            print(f"Plaintext: {plaintext}")
        else:
            print("Invalid choice. Enter 'E' or 'D'.")
        try_again = input("Try again? [Y]es or [N]o ").upper()
        if try_again[0] != 'Y':
            break
    return 0


def decrypt_matrix(key_int, cipherlist, rows):
    """Turn every n items in a list into a new item in a list of lists."""
    translation_matrix = [None] * len(key_int)
    start = 0
    stop = rows
    for k in key_int:
        if k < 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # read top-to-bottom of column
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += rows
        stop += rows
    return translation_matrix


def decrypt(ciphertext, key):
    """Decrypt a route cipher given the ciphertext and key."""
    # split elements into words
    cipherlist = list(ciphertext.split())
    key_int = [int(i) for i in key.split()]
    rows = int(len(cipherlist) / len(key_int))
    translation_matrix = decrypt_matrix(key_int, cipherlist, rows)
    plaintext = ''
    for i in range(rows):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


def encrypt_matrix(key_int, wordlist, rows):
    """Build the translation matrix. Number of columns = length of key"""
    cols = len(key_int)
    translation_matrix = [None] * rows
    start = 0
    stop = cols
    for i in range(rows):
        translation_matrix[i] = wordlist[start:stop]
        start += cols
        stop += cols
    return translation_matrix


def rotate_matrix(original):
    """Rotates the matrix 90 degrees clockwise"""
    return list(zip(*original[::-1]))


def encrypt(plaintext, key):
    """Encrypt a route cipher given the ciphertext and key."""
    wordlist = list(plaintext.split())
    key_int = [int(i) for i in key.split()]
    rows = int(len(wordlist) / len(key_int))
    encryption_matrix = encrypt_matrix(key_int, wordlist, rows)
    # rotate the matrix so we can index by columns
    # note: this means that in the rotated matrix
    # the first column is the first row, but backwards
    encryption_matrix = rotate_matrix(encryption_matrix)
    ciphertext = ''
    for k in key_int:
        col_items = encryption_matrix[abs(k)-1]
        if k > 0:  # read from the old top, so reverse the list
            col_items = col_items[::-1]
        for item in col_items:
            ciphertext += str(item) + ' '
    return ciphertext.strip()


if __name__ == '__main__':
    sys.exit(main())
