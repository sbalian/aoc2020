#!/usr/bin/env python


def read_world(path):
    with open(path) as f:
        return f.read().strip().split("\n")


def count_trees(world, right, down):
    width = len(world[0])

    level = down
    num_trees = 0

    i = 1
    while True:
        try:
            if world[level][(right * i) % width] == "#":
                num_trees += 1
        except IndexError:
            return num_trees
        i += 1
        level += down


def main():
    world = read_world("input.txt")

    assert count_trees(world, 3, 1) == 159

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod = 1
    for right, down in slopes:
        prod *= count_trees(world, right, down)
    assert prod == 6419669520
    print("All tests passed.")


if __name__ == "__main__":
    main()
