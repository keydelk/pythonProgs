#!/usr/bin/env python3

r"""Encrypt a Civil War 'rail fence' type cypher.
This is for a '2-rail' fence cipher for short messages.

Example text to encrypt: 'Buy more Maine potatoes'.

Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S

Read zigzag:        \/\/\/\/\/\/\/\/\/\

Encrypted: BYOEA NPTTE UMRMI EOSOS
"""

# ------------------------------------------------------------------------------
# USER INPUT is now prompted

# The string to be encrypted (enter between quotes):
# plaintext = """Let us cross over the river and rest under the shade of the trees
# """

# END OF USER INPUT
# ------------------------------------------------------------------------------


def main():
    """Run program to encrypt message using 2-rail rail fence cipher."""
    plaintext = input("Enter plaintext: ")
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing whitespace."""
    message = "".join(plaintext.split())
    message = message.upper()  # convention for ciphertext is uppercase
#    print("\nplaintext = {}".format(plaintext))  # uncomment for debugging
    return message


def build_rails(message):
    """Build strings with every other letter in a message."""
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails


def encrypt(rails):
    """Split letters in ciphertext into chunks of 5 & join to make string."""
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print(f"{ciphertext}")


if __name__ == '__main__':
    main()
