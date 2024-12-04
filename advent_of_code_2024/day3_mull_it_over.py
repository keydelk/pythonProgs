#!/usr/bin/env python3
# URL: https://adventofcode.com/2024/day/3
import sys
import re


def parse_line(line):
    return re.findall(
        r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)",
        line)


def parse_operands(expression):
    lst = re.findall("[0-9]+", expression)
    return int(lst[0]), int(lst[1])


lines = sys.stdin.readlines()
result = 0
do = True

for line in lines:
    print(line)
    expressions = parse_line(line)
    print(f"\tExpression: {expressions}")
    for expression in expressions:
        if expression == "do()":
            do = True
            print("\t\tDo:")
        elif expression == "don't()":
            do = False
            print("\t\tDon't:")
        else:
            if do:
                a, b = parse_operands(expression)
                print(f"\t\ta = {a}, b = {b}")
                result += a * b

print(result)
