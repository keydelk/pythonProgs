#!/usr/bin/env python3
r"""Decrypt a Civil War 'rail fence' type cipher.

This is for a 2-rail fence cipher for short messages.

Example plaintext: 'Buy more Maine potatoes'

Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S

Read zigzag:        \/\/\/\/\/\/\/\/\/\

Ciphertext: BYOEA NPTTE UMRMI EOSOS
"""
import math
import itertools
# ------------------------------------------------------------------------------
# USER INPUT IS NOW PROMPTED FROM THE USER
# the string to be decrypted (between quotes):
# ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES
# """

# END OF USER INPUT
# ------------------------------------------------------------------------------


def main():
    """Run program to decrypt 2-rail fence cipher."""
    ciphertext = input()
    print(decrypt(ciphertext))


def prep_ciphertext(ciphertext):
    """Remove whitespace"""
    message = "".join(ciphertext.split())
#    print(f"ciphertext = {ciphertext}") # uncomment for debugging
    return message


def split_rails(message):
    """Split message in two, always rounding up on 1st row."""
    row_1_len = math.ceil(len(message)/2)
    row1 = (message[:row_1_len]).lower()
    row2 = (message[row_1_len:]).lower()
    return row1, row2


def decrypt(ciphertext):
    """Build list with every other letter in 2 strings and print."""
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()
    return "".join(plaintext)




if __name__ == '__main__':
    main()
