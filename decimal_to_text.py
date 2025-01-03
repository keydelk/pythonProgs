#!/usr/bin/env python3
# Converts a string of space separated decimal digits into strings of ASCII
import sys


def parse_char(digits):
    val = int(digits)
    character = ''
    try:
        character = chr(val)
    except UnicodeEncodeError:
        character = '?'
    finally:
        return character


cipher_text = sys.stdin.readlines()
plain_text = ''

for line in cipher_text:
    for seq in line.split(' '):
        plain_text += parse_char(seq)


print(plain_text)
