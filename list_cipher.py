#!/usr/bin/env python3
"""Hides plaintext message as a null cipher in a list."""
from random import randint
import string
import load_dictionary

def hide_message(message, word_list):
    """build a list using the message and word-list"""
