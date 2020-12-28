#!/usr/bin/env python


import enum
from collections import defaultdict

import numpy as np


def int_sqrt(number):
    v = 1
    while number != v * v:
        v += 1
    return v


class Orientation(enum.Enum):
    M0 = enum.auto()
    M1 = enum.auto()
    M2 = enum.auto()
    M3 = enum.auto()
    U0 = enum.auto()
    U1 = enum.auto()
    U2 = enum.auto()
    U3 = enum.auto()


class Side(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    TOP = enum.auto()
    BOTTOM = enum.auto()


def equal(array1, array2):
    return (array1 == array2).all()


class Tile:
    def __init__(self, id_, array):
        self.id_ = id_
        self._arrays = self._make_arrays(array)

    def _make_arrays(self, array):
        array = np.array(array)
        u_array = np.flipud(array)
        return {
            Orientation.M0: array,
            Orientation.M1: np.rot90(array, 1),
            Orientation.M2: np.rot90(array, 2),
            Orientation.M3: np.rot90(array, 3),
            Orientation.U0: u_array,
            Orientation.U1: np.rot90(u_array, 1),
            Orientation.U2: np.rot90(u_array, 2),
            Orientation.U3: np.rot90(u_array, 3),
        }

    def array(self, orientation):
        return self._arrays[orientation]

    def side(self, orientation, side):
        if side == Side.LEFT:
            return self.array(orientation)[:, 0]
        elif side == Side.RIGHT:
            return self.array(orientation)[:, -1]
        elif side == Side.TOP:
            return self.array(orientation)[0, :]
        elif side == Side.BOTTOM:
            return self.array(orientation)[-1, :]
        else:
            raise ValueError(f"invalid side '{side}'")

    def __repr__(self):
        return f"{self.id_}"


def read_tiles(path):
    with open(path) as f:
        lines = f.read().strip().split("\n\n")
    tiles = []
    for line in lines:
        line = line.split("\n")
        id_ = int(line[0].replace("Tile ", "").rstrip(":"))
        line = line[1:]
        array = [[char for char in row] for row in line]
        tiles.append(Tile(id_, array))
    return tiles


def reassemble(tiles):

    neighbors = {}

    for t in tiles:
        neighbors[t] = {}
        for o in Orientation:
            neighbors[t][o] = defaultdict(list)
            for s in tiles:
                if t.id_ == s.id_:
                    continue
                for p in Orientation:
                    for q in Side:
                        for r in Side:
                            if q == r:
                                continue
                            if equal(t.side(o, q), s.side(p, r)):
                                neighbors[t][o][q].append((s, p, r))

    n = int_sqrt(len(neighbors.keys()))
    corners = [k for k, v in neighbors.items() if len(v[Orientation.M0]) == 2]

    grid = {}

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                first_corner = corners[0]
                for o in Orientation:
                    sides = neighbors[first_corner][o]
                    if Side.RIGHT in sides and Side.BOTTOM in sides:
                        grid[(0, 0)] = (corners[0], o)
                        # break  # comment to pick the example ...
            elif j == 0:
                top_tile, top_orientation = grid[(i - 1, 0)]
                for tile in neighbors[top_tile][top_orientation][Side.BOTTOM]:
                    id_, o, s = tile
                    if s == Side.TOP:
                        grid[(i, 0)] = (id_, o)
                        break
            else:
                left_tile, left_orientation = grid[(i, j - 1)]
                for tile in neighbors[left_tile][left_orientation][Side.RIGHT]:
                    id_, o, s = tile
                    if s == Side.LEFT:
                        grid[(i, j)] = (id_, o)
                        break

    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            tile, orientation = grid[(i, j)]
            array = tile.array(orientation)
            array = array[1:-1, 1:-1]
            row.append(array)
        row = np.concatenate(tuple(row), axis=1)
        rows.append(row)

    return np.concatenate(tuple(rows), axis=0), corners


def find_monster(start, picture):
    diffs = [
        (0, 0),
        (1, 1),
        (0, 3),
        (-1, 1),
        (0, 1),
        (1, 1),
        (0, 3),
        (-1, 1),
        (0, 1),
        (1, 1),
        (0, 3),
        (-1, 1),
        (0, 1),
        (-1, 0),
        (1, 1),
    ]
    i, j = start

    indices = []

    for diff in diffs:
        i += diff[0]
        j += diff[1]
        try:
            if picture[i, j] == "#":
                indices.append((i, j))
            else:
                return
        except IndexError:
            return

    return indices


def find_monsters(picture):
    monsters = []
    n = picture.shape[0]
    for i in range(n):
        for j in range(n):
            monster = find_monster((i, j), picture)
            if monster is not None:
                monsters.append(monster)
    return monsters


def print_picture(picture):
    to_print = ""
    n = len(picture)
    for i in range(n):
        for j in range(n):
            to_print += picture[i][j]
        to_print += "\n"
    print(to_print.rstrip("\n"))


def part1(corners):
    prod = 1
    for corner in corners:
        prod *= corner.id_
    return prod


def part2(picture):
    picture = Tile(-1, picture)
    for orientation in Orientation:
        monsters = find_monsters(picture.array(orientation))
        if monsters != []:
            break
    monsters = [x for y in monsters for x in y]

    picture = picture.array(orientation)

    for i, j in monsters:
        picture[i, j] = "O"

    unique, counts = np.unique(picture, return_counts=True)
    return dict(zip(unique, counts))["#"]


def main():
    tiles = read_tiles("input.txt")
    picture, corners = reassemble(tiles)
    assert part1(corners) == 20913499394191
    assert part2(picture) == 2209
    print("All tests passed.")


if __name__ == "__main__":
    main()
