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
            mask = {}
            for i, char in enumerate(extract_mask(line)):
                if char != "0":
                    mask[i] = char
        else:
            address, value = extract_address_value(line)
            address = str(bin(address))[2:].zfill(36)
            new_address = []
            for i, char in enumerate(address):
                if i in mask:
                    new_address.append(mask[i])
                else:
                    new_address.append(char)
            num_floating = new_address.count("X")
            floating = []
            for i in range(2 ** num_floating):
                floating.append(bin(i)[2:].zfill(num_floating))

            addresses = []
            for f in floating:
                to_insert = list(f)
                final_address = []
                j = 0
                for char in new_address:
                    if char == "X":
                        final_address.append(to_insert[j])
                        j += 1
                    else:
                        final_address.append(char)
                addresses.append("".join(final_address))
            for x in addresses:
                array[int(x, 2)] = value
    return sum(array.values())


def main():
    program = read_program("input.txt")
    assert part1(program) == 17934269678453
    assert part2(program) == 3440662844064
    print("All tests passed.")


if __name__ == "__main__":
    main()


# for i in range(2**5):
#     print()
