#!/usr/bin/env python3
# Problem URL: https://adventofcode.com/2024/day/5
import sys


def rule_met(update, rule):
    # print(f"\tChecking rule: {rule}")
    for i in range(len(update)):
        if update[i] == rule[1]:
            failure = (rule[0] in update[i:])
            # print(f"\t\tConsequent {rule[1]} found. Failure = {failure}")
            return not failure
    # print("\t\tConsequent not found, rule does not apply.")
    return True


def update_satisfies_rules(update, rules):
    # print(f"Checking update: {update}")
    for rule in rules:
        if not rule_met(update, rule):
            return False
    # print("Update meets all rules.")
    return True


def middle_value(update):
    midpoint = int(len(update) / 2)
    mid_val = int(update[midpoint])
    # print(f"Mid Value: {mid_val}")
    return mid_val


def fix_violation(update, rule):
    """Swap the position of the elements to fix the rule"""
    index_a = update.index(rule[0])
    index_b = update.index(rule[1])
    update[index_a] = rule[1]
    update[index_b] = rule[0]


def fix_violations(update, rules):
    # print(f"fixing: {update}")
    passes = 0
    while not update_satisfies_rules(update, rules):
        passes += 1
        # print(f"\tPass = {passes}")
        for rule in rules:
            if not rule_met(update, rule):
                # print(f"\t\tSwapping {rule}")
                fix_violation(update, rule)
    # print(update)


rules = []
updates = []
data = sys.stdin.readlines()
result = 0

for line in data:
    # print(line)
    if '|' in line:
        rule = line.strip().split('|')
        rules.append(rule)
    elif line.strip():
        update = line.strip().split(',')
        updates.append(update)

for update in updates:
    if not update_satisfies_rules(update, rules):
        fix_violations(update, rules)
        result += middle_value(update)

# print(rules)
# print(updates)

print(result)
