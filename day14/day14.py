#!/usr/bin/env python

import re


def read_program(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    return lines


def extract_mask(line):
    return re.match(r"mask = (?P<mask>.*)", line).group("mask")


def extract_address_value(line):
    m = re.match(r"mem\[(?P<address>.*)\] = (?P<value>.*)", line)
    return int(m.group("address")), int(m.group("value"))


def part1(program):
    array = {}
    for line in program:
        if line.startswith("mask"):
            mask = extract_mask(line)
        else:
            address, value = extract_address_value(line)
            array[address] = (value | int(mask.replace("X", "0"), 2)) & int(
                mask.replace("X", "1"), 2
            )
    return sum(array.values())


def part2(program):
    array = {}
    for line in program:
        if line.startswith("mask"):
            mask = extract_mask(line)
        else:
            address, value = extract_address_value(line)
            address = address | int(mask.replace("X", "0"), 2)
            template = list(str(bin(address))[2:].zfill(36))
            num_floating = 0
            for i, m in enumerate(mask):
                if m == "X":
                    num_floating += 1
                    template[i] = "{}"
            template = "".join(template)
            for i in range(2 ** num_floating):
                address = template.format(
                    *tuple(str(bin(i))[2:].zfill(num_floating))
                )
                array[address] = value
    return sum(array.values())


def main():
    program = read_program("input.txt")
    assert part1(program) == 17934269678453
    assert part2(program) == 3440662844064
    print("All tests passed.")


if __name__ == "__main__":
    main()
