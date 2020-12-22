#!/usr/bin/env python


from collections import defaultdict

import numpy as np


def read_tiles(path):
    with open(path) as f:
        tiles = f.read().strip().split("\n\n")
    tiles_ = {}
    for line in tiles:
        line = line.split("\n")
        id_ = int(line[0].replace("Tile ", "").rstrip(":"))
        line = line[1:]
        array = [[char for char in row] for row in line]
        tiles_[id_] = np.array(array)
    return tiles_


def get_corners(a):
    corners = [a[:, 0], a[0, :], a[:, -1], a[-1, :]]
    corners.extend([np.array(list(reversed(x))) for x in corners])
    return corners


def part1(tiles):
    tile_ids = list(tiles.keys())
    num_neighbors = defaultdict(int)
    n = len(tile_ids)

    for i in range(n):
        j = 0
        while j < i:
            first_tile = tile_ids[i]
            second_tile = tile_ids[j]
            c1 = get_corners(tiles[first_tile])
            c2 = get_corners(tiles[second_tile])
            for w in c1:
                for q in c2:
                    if (w == q).all():
                        num_neighbors[first_tile] += 1
                        num_neighbors[second_tile] += 1
            j += 1

    min_value = min(num_neighbors.values())
    prod = 1
    for tile in num_neighbors:
        if num_neighbors[tile] == min_value:
            prod *= tile
    return prod


def main():
    tiles = read_tiles("input.txt")
    assert part1(tiles) == 20913499394191
    print("All tests passed.")


if __name__ == "__main__":
    main()
