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


    # split elements into words
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(f"Plaintext = {plaintext}")


def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):  # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print(f"Length of cipher = {len_cipher}")
    print(f"Acceptable column/row values include: {factors}")
    print()
    if ROWS * COLS != len_cipher:
        print("Error - Input columns and rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)


def key_to_int(key):
    """Turn key into list of integers & check validity."""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
       or 0 in key_int:
        print("Error - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int


def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # read top-to-bottom of column
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix


def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext

if __name__ == '__main__':
    sys.exit(main())
