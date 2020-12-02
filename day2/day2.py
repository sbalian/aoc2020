#!/usr/bin/env python


def read_lines(path):
    with open(path) as f:
        return f.read().strip().split("\n")


def num_valid1(path):
    lines = read_lines(path)
    valid = 0
    for line in lines:
        range_, char, passwd = line.split()
        min, max = range_.split("-")
        min, max = int(min), int(max)
        char = char.replace(":", "")
        if min <= passwd.count(char) <= max:
            valid += 1
    return valid


def num_valid2(path):
    lines = read_lines(path)
    valid = 0
    for line in lines:
        pos, char, passwd = line.split()
        pos1, pos2 = pos.split("-")
        pos1, pos2 = int(pos1), int(pos2)
        char = char.replace(":", "")
        if (passwd[pos1 - 1] == char) + (passwd[pos2 - 1] == char) == 1:
            valid += 1
    return valid


def main():
    assert num_valid1("input.txt") == 500
    assert num_valid2("input.txt") == 313
    print("All tests passed.")


if __name__ == "__main__":
    main()
