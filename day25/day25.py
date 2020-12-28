#!/usr/bin/env python


INPUT = [9789649, 3647239]


def find_loop_size(subject_matter, public_key, max_i=100000000):
    value = 1
    for i in range(max_i):
        value = (value * subject_matter) % 20201227
        if value == public_key:
            return i + 1


def transform_subject_number(subject_matter, loop_size):
    value = 1
    for i in range(loop_size):
        value = (value * subject_matter) % 20201227
    return value


def part1():
    public_key1, public_key2 = INPUT
    loop_size1 = find_loop_size(7, public_key1)
    return transform_subject_number(public_key2, loop_size1)


def main():
    assert part1() == 8740494
    print("All tests passed.")


if __name__ == "__main__":
    main()
