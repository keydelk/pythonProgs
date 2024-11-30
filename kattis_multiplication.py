#!/usr/bin/env python3

# Kattis Problem: More Multiplication
# URL: https://open.kattis.com/problems/multiplication
# Description:
# Educators are always coming up with new ways to teach math to students.
# In 2011, an educational software company, All Computer Math (ACM), developed
# an application to display products in a traditional grade school math format.
# ACM is now working on an updated version of the software that will display
# results in a lattice format that some students find to be easier when
# multiplying larger numbers. E.g. when multiplying 345 * 56 = 19320
# as given below, using a lattice grid with 2 rows and 3 columns, which appears
# inside a surrounding frame:
#  +---------------+
#  |   3   4   5   |
#  | +---+---+---+ |
#  | |1 /|2 /|2 /| |
#  | | / | / | / |5|
#  |1|/ 5|/ 0|/ 5| |
#  | +---+---+---+ |
#  |/|1 /|2 /|3 /| |
#  | | / | / | / |6|
#  |9|/ 8|/ 4|/ 0| |
#  | +---+---+---+ |
#  |/ 3 / 2 / 0    |
#  +---------------+
# The first operand, 345, is displayed above the top of the grid with each
# digit centered horizontally above its column of the grid, and the second
# operand, 56, is displayed along the righthand side with each digit centered
# vertically at the center of its row in the grid. A single cell of the grid,
#          +---+
#          |3 /|
#          | / |
#          |/ 0|
#          +---+
# represnts the product of the digit of the first operand that is above its
# column and the digit of the second operand that is to the right of its row.
# In our example, this cell represnts the product 5 * 6 = 30 that results when
# multiplying the 5 in 345 and the 6 in 56. Note that the 10's digit of that
# product is placed in the upper left portion of this cell adn the 1's digit in
# the lower right.
# The overall product is then computed by summing along the diagonals in the
# lattice that represtnts the same place values in the results. E.g.
#     1’s digit = 0
#    10’s digit = 5 + 3 + 4 = 12, thus 2 with a carry of 1
#   100’s digit = (1 carry) + 2 + 0 + 2 + 8 = 13, thus 3 with a carry of 1
#  1000’s digit = (1 carry) + 2 + 5 + 1 = 9
# 10000’s digit = 1
# The product is placed with the one’s digit below the grid at the far
# right and, depending on its length, with the most significant digits wrapped
# around the left side of the grid. Each digit of the final product appears
# perfectly aligned with the corresponding diagonal summands.
#
# Input:
# The input is composed of T test cases 1 <= T <= 20
# Each test case contains 2 positive integers, A and B,  1 <= A or B <= 9999
# The last test case will be followed by a line containing 0 0
#
# Output:
# For each test case produce the grid that illustrates how to multiply two
# numbers using the lattice method above. Grids are printed to stdout
# one following another.
import math
import sys
input = sys.stdin.readline

# read test cases in a loop
test_cases = []
while True:
    a, b = map(int, input().split())
    tc = (a, b)
    if tc == (0, 0):
        break
    test_cases.append(tc)

for tc in test_cases:
    a = tc[0]
    b = tc[1]
    a_string = str(a)
    b_string = str(b)
    a_digits = len(a_string)
    b_digits = len(b_string)
    ab = a * b
    ab_string = str(ab)
    ab_digits = len(ab_string)
    ab_padded = ab_string.rjust((a_digits+b_digits), ' ')

    top_border = "+-" + a_digits * "----" + "--+"
    first_line = "| "
    for i in range(a_digits):
        first_line += f"  {a_string[i]} "
    first_line += "  |"
    inner_border = "| " + a_digits * "+---" + "+ |"
    grid = ""
    for i in range(b_digits):
        if (b_digits - i) < (ab_digits - a_digits):
            grid += "|/"
        else:
            grid += "| "
        for j in range(a_digits):
            grid += f"|{math.floor(int(a_string[j])*int(b_string[i])/10)} /"
        grid += "| |\n"
        grid += "| " + a_digits * "| / " + f"|{b_string[i]}|\n"
        grid += f"|{ab_padded[i]}"
        for j in range(a_digits):
            grid += f"|/ {(int(a_string[j])*int(b_string[i]) % 10)}"
        grid += "| |\n"
        grid += inner_border + "\n"

    bottom_line = "|"
    if ab_digits > a_digits:
        bottom_line += "/ "
    else:
        bottom_line += "  "
    for i in range(a_digits):
        bottom_line += ab_padded[b_digits+i]
        if i < a_digits - 1:
            bottom_line += " / "
        else:
            bottom_line += "    |"

    output = top_border + '\n' + first_line + '\n' + inner_border + \
        '\n' + grid + bottom_line + '\n' + top_border
    print(output)
