#!/usr/bin/env python3
# https://adventofcode.com/2024/day/2
# Given a list of reports (rows) containing integer levels separated by spaces,
# determine how many reports are safe. A report is safe if and only if it is
# gradually increasing or gradually decreasing. Adjacent levels can differ by
# one to three and must all be in the same direction.
import sys


def right_direction(cur,  nxt, direction):
    return direction * (cur - nxt) < 0


def small_size(cur, nxt):
    return abs(cur - nxt) <= 3


def safe_levels(cur, nxt, direction):
    print(f"\t checking: {cur}, {nxt}, direction: {direction}")
    return right_direction(cur, nxt, direction) and small_size(cur, nxt)


def is_safe(levels, dampener):
    direction = 1 if levels[0] < levels[1] else -1

    for i in range(len(levels) - 1):
        if not safe_levels(levels[i], levels[i+1], direction):
            if dampener:
                print("\t\tDampener used")
                # try both removing
                minus_i = levels.copy()
                minus_i1 = levels.copy()
                del minus_i[i]
                del minus_i1[i+1]
                if i > 0:
                    minus_im = levels.copy()
                    del minus_im[i-1]
                    return is_safe(minus_i, False) or is_safe(minus_i1, False) or is_safe(minus_im, False)
                else:
                    return is_safe(minus_i, False) or is_safe(minus_i1, False)

            else:
                print("\t\tUnsafe levels")
                return False

    return True


reports = sys.stdin.readlines()
number_safe = 0

for report in reports:
    print(f"Checking report: {report}")
    levels = [int(x) for x in report.strip().split(' ')]
    if is_safe(levels, True):
        number_safe += 1
        print(f"  Report Safe.\tSafe Reports so far: {number_safe}")

print(number_safe)
