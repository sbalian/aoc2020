#!/usr/bin/env python


import collections
import itertools


def get_deltas(n):
    return list(
        set(itertools.permutations(n * [1] + (n - 1) * [0] + n * [-1], n))
    )


def add_coords(a, b):
    n = len(a)
    # assert n == len(b)
    return tuple(a[i] + b[i] for i in range(n))


class Simulator:
    def __init__(self, grid_path, dimension):
        self.dimension = dimension
        self.deltas = get_deltas(dimension)

        with open(grid_path) as f:
            grid = f.read().strip().split("\n")
        self.active = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                to_add = tuple([row, col] + (self.dimension - 2) * [0])
                if grid[row][col] == "#":
                    self.active.add(to_add)

    def get_neighbors(self, point):
        return (add_coords(point, delta) for delta in self.deltas)

    def evolve_one_step(self):
        to_deactivate = set()

        inactive = collections.defaultdict(int)

        for active_cube in self.active:
            num_active = 0
            for neighbor in self.get_neighbors(active_cube):
                if neighbor in self.active:
                    num_active += 1
                else:
                    inactive[neighbor] += 1
            if num_active < 2 or num_active > 3:
                to_deactivate.add(active_cube)

        for cube in inactive:
            if inactive[cube] == 3:
                self.active.add(cube)

        self.active -= to_deactivate

    def evolve(self, steps):
        [self.evolve_one_step() for _ in range(steps)]
        return self.num_active()

    def num_active(self):
        return len(self.active)


def main():
    grid_path = "input.txt"
    assert Simulator(grid_path, dimension=3).evolve(steps=6) == 336
    assert Simulator(grid_path, dimension=4).evolve(steps=6) == 2620
    print("All tests passed.")


if __name__ == "__main__":
    main()
