#!/usr/bin/env python

import copy


def get_grid(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    return [list(line) for line in lines]


def answer(grid, step_fn):
    previous_grid = grid
    grid = step_fn(grid)

    while grid != previous_grid:
        previous_grid = grid
        grid = step_fn(grid)

    occupied = 0
    for row in grid:
        occupied += row.count("#")
    return occupied


def get_neighbors(position, w, h):
    x, y = position
    if x == y == 0:
        return [(0, 1), (1, 0), (1, 1)]
    elif x == 0 and y == w:
        return [(0, w - 1), (1, w), (1, w - 1)]
    elif y == 0 and x == h:
        return [(h, 1), (h - 1, 0), (h - 1, 1)]
    elif x == h and y == w:
        return [(h, w - 1), (h - 1, w - 1), (h - 1, w)]
    elif y == 0:
        return [(x - 1, 0), (x + 1, 0), (x - 1, 1), (x + 1, 1), (x, 1)]
    elif x == 0:
        return [(0, y - 1), (0, y + 1), (1, y - 1), (1, y + 1), (1, y)]
    elif x == h:
        return [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y),
        ]
    elif y == w:
        return [
            (x - 1, y),
            (x + 1, y),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x, y - 1),
        ]
    else:
        return [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y - 1),
        ]


def step1(grid):
    h = len(grid)
    w = len(grid[0])

    new_grid = copy.deepcopy(grid)

    for i in range(h):
        for j in range(w):
            position = (i, j)
            seat = grid[i][j]
            neighbors = []
            for x, y in get_neighbors(position, w - 1, h - 1):
                neighbors.append(grid[x][y])
            if seat == "L" and "#" not in neighbors:
                new_grid[i][j] = "#"
            if seat == "#" and neighbors.count("#") > 3:
                new_grid[i][j] = "L"
    return new_grid


def get_seen(position, grid):
    x, y = position

    all_seen = []

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x + i][y]
        except IndexError:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x - i][y]
        except IndexError:
            break
        if (x - i) < 0:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x][y + i]
        except IndexError:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x][y - i]
        except IndexError:
            break
        if (y - i) < 0:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x + i][y + i]
        except IndexError:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x - i][y - i]
        except IndexError:
            break
        if (x - i) < 0 or (y - i) < 0:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x + i][y - i]
        except IndexError:
            break
        if (y - i) < 0:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    seen = "."
    i = 1
    while True:
        try:
            seen = grid[x - i][y + i]
        except IndexError:
            break
        if (x - i) < 0:
            break
        if seen != ".":
            all_seen.append(seen)
            break
        i += 1

    return all_seen


def step2(grid):
    h = len(grid)
    w = len(grid[0])

    new_grid = copy.deepcopy(grid)

    for i in range(h):
        for j in range(w):
            position = (i, j)
            seat = grid[i][j]
            seen = get_seen(position, grid)
            if seat == "L" and "#" not in seen:
                new_grid[i][j] = "#"
            if seat == "#" and seen.count("#") > 4:
                new_grid[i][j] = "L"
    return new_grid


def main():
    grid = get_grid("input.txt")
    assert answer(grid, step1) == 2344
    assert answer(grid, step2) == 2076
    print("All tests passed.")


if __name__ == "__main__":
    main()
