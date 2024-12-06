#!/usr/bin/env python3
# URL: https://adventofcode.com/2024/day/4#part2
import sys


def is_x_mas(i, j, word_search):
    """Checks if the letter at word_search[i][j] is the center A in an X-MAS"""
    if word_search[i][j] != 'A':
        return False
    elif (word_search[i-1][j-1] == 'M' and word_search[i-1][j+1] == 'S' and
            word_search[i+1][j-1] == 'M' and word_search[i+1][j+1] == 'S'):
        return True
    # 90 degree rotation
    elif (word_search[i-1][j-1] == 'M' and word_search[i-1][j+1] == 'M' and
            word_search[i+1][j-1] == 'S' and word_search[i+1][j+1] == 'S'):
        return True
    # 180 degree rotation
    elif (word_search[i-1][j-1] == 'S' and word_search[i-1][j+1] == 'M' and
            word_search[i+1][j-1] == 'S' and word_search[i+1][j+1] == 'M'):
        return True
    # 270 degree rotation
    elif (word_search[i-1][j-1] == 'S' and word_search[i-1][j+1] == 'S' and
            word_search[i+1][j-1] == 'M' and word_search[i+1][j+1] == 'M'):
        return True
    else:
        return False


word_search = sys.stdin.readlines()
num_rows = len(word_search)
num_cols = len(word_search[0])
x_mases = 0

for i in range(1, num_rows - 1):
    for j in range(1, num_cols - 1):
        if is_x_mas(i, j, word_search):
            x_mases += 1

print(x_mases)
