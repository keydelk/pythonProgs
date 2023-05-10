#!/usr/bin/env python3
"""Translate a string from English to Pig-Latin."""

def main():
    """Translate from English to Pig-Latin."""
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    txt = input("Enter text to translate into Pig-Latin: ")
    outp = ""

    for word in txt.split(" "):
        consonants = ""
        for char in word:
            if char in vowels:
                break
            consonants = consonants + char
        suffix = "way " if not consonants else consonants + "ay "
        outp = outp + word.lstrip(consonants) + suffix

    print(outp)

if __name__ == "__main__":
    main()
