#!/usr/bin/env python3
# URL: https://adventofcode.com/2024/day/7
import sys
import math


def can_be_made_true(test_value, terms):
    num_terms = len(terms)
    num_operators = num_terms - 1
    num_possible_equations = 3**num_operators
    # print(f"Test value: {test_value} \tNum Terms: {num_terms}")
    # print(terms)
    # print(f"\tNum Possible equations: {num_possible_equations}")
    for i in range(num_possible_equations):
        val = terms[0]
        test_str = str(val)
        for j in range(num_operators):
            if math.floor(i/(3**j)) % 3 == 0:
                val *= terms[j+1]
                test_str += '*' + str(terms[j+1])
            elif math.floor(i/(3**j)) % 3 == 1:
                val += terms[j+1]
                test_str += '+' + str(terms[j+1])
            else:
                str_val = str(val) + str(terms[j+1])
                val = int(str_val)
                test_str += '||' + str(terms[j+1])
        # print(f"\t{i}: {test_str} =  {val}")
        if val == test_value:
            return True
    return False


equations = sys.stdin.readlines()
calibration_result = 0

for equation in equations:
    terms = [int(x.strip(':')) for x in equation.split(" ")]
    test_value = terms.pop(0)
    if can_be_made_true(test_value, terms):
        calibration_result += test_value

print(calibration_result)
