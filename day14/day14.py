#!/usr/bin/env python


def read_program(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    return lines


def part1(program):
    array = {}
    for line in program:
        if line.startswith("mask"):
            mask = line.split()[-1]
            mask_ = {}
            for i, char in enumerate(mask):
                if char != "X":
                    mask_[i] = char
        else:
            s = line.split()
            value = int(s[-1])
            address = int(s[0][4:][:-1])
            value = bin(value)[2:].zfill(36)
            new_value = []
            for i, char in enumerate(value):
                if i in mask_:
                    new_value.append(mask_[i])
                else:
                    new_value.append(char)
            new_value = "".join(new_value)
            array[address] = new_value
    return sum([int(x, 2) for x in array.values()])


def part2(program):
    array = {}
    for line in program:
        if line.startswith("mask"):
            mask = line.split()[-1]
            mask_ = {}
            for i, char in enumerate(mask):
                if char != "0":
                    mask_[i] = char
        else:
            s = line.split()
            value = int(s[-1])
            address = int(s[0][4:][:-1])
            address = str(bin(address))[2:].zfill(36)

            new_address = []
            for i, char in enumerate(address):
                if i in mask_:
                    new_address.append(mask_[i])
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
