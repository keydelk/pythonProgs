#!usr/bin/env python3
# Python practice
import operator as op

def print_table(operator):
    for x in range(1, 10):
        for y in range(1, 10):
            print(str(operator(x, y)), end = '\t')
        print('\n', end = '')

def foo(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def all_equal(a, b, c):
    return a == b == c

def for_console_output(func):
    def wrapper(*args, **kwargs):
        print('------------------------------------')
        print(str(func(*args, **kwargs)))
        print('------------------------------------')
    return wrapper

@for_console_output
def add(x, y):
    return x + y

