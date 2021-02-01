#!/usr/bin/env python


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
        self.cubes = {}

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                to_add = tuple([row, col] + (self.dimension - 2) * [0])
                if grid[row][col] == "#":
                    self.cubes[to_add] = True
        self._add_inactives()

    def _add_inactives(self):
        neighbors = []
        for cube, active in self.cubes.items():
            if active:
                neighbors.extend(self.get_neighbors(cube))
        for neighbor in neighbors:
            if neighbor not in self.cubes:
                self.cubes[neighbor] = False

    def get_neighbors(self, point):
        return (add_coords(point, delta) for delta in self.deltas)

    def evolve_one_step(self):
        to_activate = []
        to_inactivate = []

        for cube, active in self.cubes.items():
            num_active = 0
            for neighbor in self.get_neighbors(cube):
                if neighbor in self.cubes and self.cubes[neighbor]:
                    num_active += 1
                if num_active > 3:
                    break
            if active and num_active not in [2, 3]:
                to_inactivate.append(cube)
            elif not active and num_active == 3:
                to_activate.append(cube)

        for cube in to_activate:
            self.cubes[cube] = True
        for cube in to_inactivate:
            self.cubes[cube] = False
        self._add_inactives()

    def evolve(self, steps):
        [self.evolve_one_step() for _ in range(steps)]
        return self.num_active()

    def num_active(self):
        return sum(self.cubes.values())


def main():
    grid_path = "input.txt"
    assert Simulator(grid_path, dimension=3).evolve(steps=6) == 336
    assert Simulator(grid_path, dimension=4).evolve(steps=6) == 2620
    print("All tests passed.")


if __name__ == "__main__":
    main()
