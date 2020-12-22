#!/usr/bin/env python

import re


def get_input(path):
    with open(path) as f:
        contents = f.read().strip().split("\n\n")
    rules, messages = contents
    rules_ = {}
    rules = rules.split("\n")
    for rule in rules:
        key, value = rule.split(": ")
        if "a" or "b" in value:
            value = value.strip('"')
        rules_[key] = value
    messages = messages.split("\n")
    return rules_, messages


def build(rule, rules):
    rule = rules[rule]
    if rule in ["a", "b"]:
        return rule

    split_rule = rule.split(" | ")

    if len(split_rule) == 1:
        try:
            return f"{build(rule, rules)}"
        except KeyError:
            left, right = rule.split(" ")
            return f"{build(left, rules)}{build(right, rules)}"

    left, right = split_rule

    try:
        l1, l2 = left.split()
        left_part = f"{build(l1, rules)}{build(l2, rules)}"
    except ValueError:
        left_part = f"{build(left, rules)}"

    try:
        r1, r2 = right.split()
        right_part = f"{build(r1, rules)}{build(r2, rules)}"
    except ValueError:
        right_part = f"{build(right, rules)}"

    return ("(" + left_part + "|" + right_part + ")").replace(" ", "")


def part1(rules, messages):
    expression = "^"
    for rule in rules["0"].split(" "):
        expression += build(rule, rules)
    expression += "$"
    r = re.compile(expression)
    valid = 0
    for message in messages:
        if r.match(message) is not None:
            valid += 1
    return valid


def rule11(s, e42, e31, n=0, max_n=5):
    if n == max_n:
        return f"({e42}" + s + f"{e31})"
    return f"({e42}{e31}|{e42}" + rule11(s, e42, e31, n=n + 1) + f"{e31})"


def part2(rules, messages):

    del rules["8"]
    del rules["11"]
    del rules["0"]

    e42 = build("42", rules)
    e31 = build("31", rules)

    expression = f"^({e42})+" + rule11("", e42, e31) + "$"

    valid = 0
    for message in messages:
        if re.fullmatch(expression, message):
            valid += 1

    return valid


def main():
    rules, messages = get_input("input.txt")
    assert part1(rules, messages) == 134
    assert part2(rules, messages) == 377
    print("All tests passed.")


if __name__ == "__main__":
    main()
