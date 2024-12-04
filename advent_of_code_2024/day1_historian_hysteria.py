#!/usr/bin/env python3
# https://adventofcode.com/2024/day/1
# Help the historians reconcile their lists of location IDs
# Sort the lists in order of size and find the difference between each pair of
# numbers. Print the sum of the differences.
import sys

data = sys.stdin.readlines()

left_list = []
right_list = []
dist = 0

for row in data:
    left_list.append(int(row.split('  ')[0]))
    right_list.append(int(row.split('  ')[1].strip()))
left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    dist += abs(left_list[i] - right_list[i])

print(f"distance = {dist}")

similarity_score = 0

for i in left_list:
    similarity_score += i * right_list.count(i)

print(f"Similarity score = {similarity_score}")
