#!/usr/bin/env python3
# Advent of Code URL: https://adventofcode.com/2024/day/9


def expand_disk_map(disk_map):
    expanded_map = []
    for i in range(len(disk_map)):
        val = int(disk_map[i])
        if (i % 2 == 0):
            for j in range(val):
                expanded_map.append(str(i//2))
        else:
            for j in range(val):
                expanded_map.append('.')
    return expanded_map


def compact_blocks(block_map):
    compacted_map = []
    i = 0
    j = len(block_map) - 1
    while i <= j:
        if block_map[i] != '.':
            compacted_map.append(block_map[i])
            i += 1
        else:
            while block_map[j] == '.':
                j -= 1
            compacted_map.append(block_map[j])
            i += 1
            j -= 1

    return compacted_map


def swap_region(block_map, file_id, file_len, from_pos, to_pos):
    # print(f"Moving file {file_id} from {from_pos} to {to_pos}")
    for i in range(file_len):
        block_map[to_pos-i] = file_id
        block_map[from_pos+i] = '.'


def safe_compact(block_map,):
    bmp = len(block_map) - 1  # block_map pointer
    file_id = block_map[bmp]  # we're going to check each file only 1 time
    while (bmp > 1):  # work backwards over the map
        # find the start of the file from right
        if block_map[bmp] != file_id:
            bmp -= 1
            continue

        file_len = 0
        while block_map[bmp] == file_id:  # find the length of the file
            file_len += 1
            bmp -= 1

        if int(file_id) % 100 == 0:
            print(f"\nCheck file_id: {file_id} len: {file_len} left: {bmp+1}")
        # print(block_map)

        # Find the first free region big enough for the file
        free_region = 0
        for i in range(bmp):  # search from the beginning to the pointer
            if block_map[i] != '.':
                free_region = 0
                continue
            else:
                free_region += 1
                if free_region >= file_len:
                    swap_region(block_map, file_id, file_len, bmp+1, i)
                    break
        file_id = str(int(file_id) - 1)


def calculate_checksum(compacted_map):
    checksum = 0
    # remove freespace from end
    seq = compacted_map
    for i in range(len(seq)):
        if seq[i] != '.':
            val = int(seq[i])
            checksum += val * i
    return checksum


disk_map = input()
block_map = expand_disk_map(disk_map)
# print(f"block_map: {block_map}")

# compacted_map = compact_blocks(block_map)
safe_compact(block_map)
checksum = calculate_checksum(block_map)

# print(f"compacted_map: {compacted_map}")
print(f"checksum: {checksum}")
