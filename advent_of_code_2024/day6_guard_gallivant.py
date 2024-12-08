#!/usr/bin/env python3
# Problem URL: https://adventofcode.com/2024/day/6
import sys


GUARD_NORTH = '^'
GUARD_EAST = '>'
GUARD_SOUTH = 'v'
GUARD_WEST = '<'
OBSTACLE = '#'
TRAIL = 'X'

inmap = sys.stdin.readlines()
num_rows = len(inmap)
num_cols = len(inmap[0].strip())
gmap = []
for row in inmap:
    lrow = list(row.strip())
    gmap.append(lrow)

guard_row = -1
guard_col = -1
trail_len = 0
guard_facing = GUARD_NORTH
step = 0


def leaving_next_step():
    """Returns true if the guard is on the edge of the map and facing out."""
    if guard_facing == GUARD_NORTH and guard_row == 0:
        return True
    elif guard_facing == GUARD_EAST and guard_col == num_cols - 1:
        return True
    elif guard_facing == GUARD_SOUTH and guard_row == num_cols - 1:
        return True
    elif guard_facing == GUARD_WEST and guard_col == 0:
        return True
    else:
        return False


def front_clear():
    """Returns false if the guard's path is blocked by '#'"""
    if guard_facing == GUARD_NORTH:
        if gmap[guard_row - 1][guard_col] == '#':
            return False
        else:
            return True
    elif guard_facing == GUARD_EAST:
        if gmap[guard_row][guard_col + 1] == '#':
            return False
        else:
            return True
    elif guard_facing == GUARD_SOUTH:
        if gmap[guard_row + 1][guard_col] == '#':
            return False
        else:
            return True
    else:
        if gmap[guard_row][guard_col - 1] == '#':
            return False
        else:
            return True


def move_guard():
    """Move the guard one step in the direction of facing, mark the trail
       and increment the trail_len counter."""
    global guard_facing
    global gmap
    global guard_row
    global guard_col
    global trail_len
    if gmap[guard_row][guard_col] != TRAIL:
        trail_len += 1
    gmap[guard_row][guard_col] = TRAIL
    if guard_facing == '^':
        guard_row -= 1
    elif guard_facing == '>':
        guard_col += 1
    elif guard_facing == 'v':
        guard_row += 1
    elif guard_facing == '<':
        guard_col -= 1
    # gmap[guard_row][guard_col] = guard_facing
    return


def turn_guard():
    global guard_facing
    global gmap
    if guard_facing == '^':
        guard_facing = '>'
    elif guard_facing == '>':
        guard_facing = 'v'
    elif guard_facing == 'v':
        guard_facing = '<'
    else:
        guard_facing = '^'
    gmap[guard_row][guard_col] = guard_facing
    return


def print_gmap():
    for row in gmap:
        print(''.join(row))
    return


# Get starting position of guard
for i in range(num_rows):
    if '^' in gmap[i]:
        guard_row = i
        break

if guard_row == -1:
    print("Guard not found.")
    exit(1)

for i in range(num_cols):
    if gmap[guard_row][i] == '^':
        guard_col = i
        break

print(f"Starting guard position: {guard_row},{guard_col}\n")
# print_gmap()

while not leaving_next_step():
    step += 1
    if front_clear():
        move_guard()
    else:
        turn_guard()
    # print(f"\n\t\t Step {step}, trail length = {trail_len}")
    # print_gmap()

step += 1
if gmap[guard_row][guard_col] != TRAIL:
    trail_len += 1

# gmap[guard_row][guard_col] = TRAIL:
# print("\n\n\t\tFINAL MAP")
# print_gmap()
print(f"\n\tTotal trail: {trail_len}")

# ---------Part 2 ---------------

