#!/usr/bin/env python3
# URL: https://adventofcode.com/2024/day/4
import sys
import re


def count_xmas(string):
    forwards = len(re.findall('XMAS', string))
    backward = len(re.findall('SAMX', string))
    return forwards + backward


word_search = sys.stdin.readlines()
num_matches = 0
num_rows = len(word_search)
num_columns = len(word_search[0].strip())
num_diagonals = num_rows + num_columns - 1

print(word_search)
print(f"\n\tnum_rows = {num_rows}")
print(f"\tnum_columns = {num_columns}")
print(f"\tnum_diagonals = {num_diagonals}")


# Search horizontally (rows)
print("\nSearching rows:")
for row in word_search:
    num_in_row = count_xmas(row)
    print(f"\t{row.strip()}\tNum in row: {num_in_row}")
    num_matches += num_in_row

# Search verically
print("\nSearching columns:")
for i in range(num_columns):
    column = ""
    for row in word_search:
        column += row[i]
    num_in_column = count_xmas(column)
    print(f"\t{column}\tNum in column: {num_in_column}")
    num_matches += num_in_column

# Search / diagonals starting from top left
print("\nSearching / diagonals")
for i in range(num_diagonals):
    diagonal = ""
    diagonal_len = min(i+1, num_rows, num_columns, (num_diagonals - i))
    start_row = min(i, num_rows-1)
    start_col = max(0, (i+1 - num_columns))
    print(f"Diagonal {i}: length = {diagonal_len}\tStarting pos: [{start_row}], [{start_col}]")
    # if the diagonal is less than 4 characters, no need to check
    # if diagonal_len < 4:
    #     continue
    for j in range(diagonal_len):
        row = start_row - j
        col = start_col + j
        diagonal += word_search[row][col]
    num_in_diagonal = count_xmas(diagonal)
    print(f"\t{diagonal}\tNum XMAS: {num_in_diagonal}")
    num_matches += num_in_diagonal

# Search \ diagonals starting from top right
print("\nSearching \\ diagonals")
for i in range(num_diagonals):
    diagonal = ""
    diagonal_len = min(i+1, num_rows, num_columns, (num_diagonals - i))
    start_row = min(i, num_rows-1)
    start_col = min(num_columns - 1, (2*num_columns - i - 2))
    print(f"Diagonal {i}: length = {diagonal_len}\tStarting pos: [{start_row}], [{start_col}]")
    # if the diagonal is less than 4 characters, no need to check
    # if diagonal_len < 4:
    #     continue
    for j in range(diagonal_len):
        row = start_row - j
        col = start_col - j
        diagonal += word_search[row][col]
    num_in_diagonal = count_xmas(diagonal)
    print(f"\t{diagonal}\tNum XMAS: {num_in_diagonal}")
    num_matches += num_in_diagonal

print("\nGrand Total:")
print(num_matches)
