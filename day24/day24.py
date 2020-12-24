#!/usr/bin/env python


import re


def read_instructions(path):
    with open(path) as f:
        return [
            [step for step in re.findall("(e|se|sw|w|nw|ne)", line)]
            for line in f.read().strip().split("\n")
        ]


def get_neighbor(tile, step):
    if step == "e":
        return (tile[0] + 1, tile[1] - 1, tile[2])
    elif step == "w":
        return (tile[0] - 1, tile[1] + 1, tile[2])
    elif step == "ne":
        return (tile[0] + 1, tile[1], tile[2] - 1)
    elif step == "nw":
        return (tile[0], tile[1] + 1, tile[2] - 1)
    elif step == "se":
        return (tile[0], tile[1] - 1, tile[2] + 1)
    elif step == "sw":
        return (tile[0] - 1, tile[1], tile[2] + 1)
    else:
        raise ValueError(f"invalid direction '{step}'")


def memoize(func):
    cache = {}

    def memoized(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]

    return memoized


@memoize
def get_neighbors(tile):
    return [
        get_neighbor(tile, direction)
        for direction in ["e", "se", "sw", "w", "nw", "ne"]
    ]


def part1(instructions):
    origin = (0, 0, 0)
    blacks = set()

    for steps in instructions:
        next_ = origin
        for step in steps:
            next_ = get_neighbor(next_, step)
        if next_ in blacks:
            blacks.remove(next_)
        else:
            blacks.add(next_)
    return blacks


def flip(blacks):

    to_turn_white = set()
    whites = set()

    for black in blacks:
        num_adjacent_black_neighbors = 0
        for neighbor in get_neighbors(black):
            if neighbor in blacks:
                num_adjacent_black_neighbors += 1
            else:
                whites.add(neighbor)
        if (num_adjacent_black_neighbors == 0) or (
            num_adjacent_black_neighbors > 2
        ):
            to_turn_white.add(black)

    to_turn_black = set()
    for white in whites:
        num_adjacent_black_neighbors = 0
        for neighbor in get_neighbors(white):
            if neighbor in blacks:
                num_adjacent_black_neighbors += 1
        if num_adjacent_black_neighbors == 2:
            to_turn_black.add(white)
    return (blacks - to_turn_white).union(to_turn_black)


def part2(blacks):
    for _ in range(100):
        blacks = flip(blacks)
    return len(blacks)


def main():
    instructions = read_instructions("input.txt")
    blacks = part1(instructions)
    assert len(blacks) == 300
    assert part2(blacks) == 3466
    print("All tests passed.")


if __name__ == "__main__":
    main()
