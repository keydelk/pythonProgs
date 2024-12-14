#!/usr/bin/env python3
# URL: https://adventofcode.com/2024/day/8
import sys


a_map = sys.stdin.readlines()
ant_dict = dict()
map_rows = len(a_map)
map_cols = len(a_map[0].strip())
antinodes = []

for i in range(map_rows):
    for j in range(map_cols):
        char = a_map[i][j]
        if char == '.' or char == '\n':
            continue
        elif char in ant_dict:
            ant_dict[char].append((i, j))
        else:
            ant_dict[char] = [(i, j)]

print(f"Num Rows: {map_rows}")
print(f"Num Cols: {map_cols}")
print(ant_dict)

for key in ant_dict:
    val = ant_dict[key]
    print(f"Checking key: {key}")
    for i in range(0, len(val) - 1):
        for j in range(i + 1, len(val)):
            displacement = (val[j][0] - val[i][0], val[j][1] - val[i][1])
            print(f"{val[i]} to {val[j]}: {displacement}")
            a = (val[i][0] - displacement[0], val[i][1] - displacement[1])
            b = (val[j][0] + displacement[0], val[j][1] + displacement[1])
            print(f"\tAntinodes a = {a}, b = {b}")
            if (a[0] < 0 or a[0] >= map_rows or a[1] < 0 or a[1] >= map_cols):
                print("\t\ta out of bounds")
            elif a not in antinodes:
                antinodes.append(a)
            if (b[0] < 0 or b[0] >= map_rows or b[1] < 0 or b[1] >= map_cols):
                print("\t\tb out of bounds")
            elif b not in antinodes:
                antinodes.append(b)

print(antinodes)
print(f"Total antinodes: {len(antinodes)}")
