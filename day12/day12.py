#!/usr/bin/env python


import math


def get_instructions(path):
    with open(path) as f:
        instructions = f.read().strip().split("\n")
    return instructions


def parse_instruction(instruction):
    return instruction[0], int(instruction[1:])


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalised(self):
        ll = self.norm()
        return Vector(self.x / ll, self.y / ll)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def rotate(self, degrees):
        rad = math.radians(degrees)
        return Vector(
            self.x * math.cos(rad) - self.y * math.sin(rad),
            self.x * math.sin(rad) + self.y * math.cos(rad),
        )

    @classmethod
    def unit(cls, degrees):
        rad = math.radians(degrees)
        return cls(math.cos(rad), math.sin(rad)).normalised()


class Ship:
    def __init__(
        self, position=Vector(0, 0), direction=0, waypoint=Vector(10, 1)
    ):
        self.position = position
        self.direction = direction  # for move of type 1
        self.waypoint = waypoint  # for move of type 2

    def move(self, instruction, move_type):
        if move_type == 1:
            self.move1(instruction)
        else:
            self.move2(instruction)

    def move1(self, instruction):
        move_, value = parse_instruction(instruction)
        if move_ == "N":
            self.position += Vector(0, value)
        elif move_ == "S":
            self.position -= Vector(0, value)
        elif move_ == "E":
            self.position += Vector(value, 0)
        elif move_ == "W":
            self.position -= Vector(value, 0)
        elif move_ == "R":
            self.direction -= value
        elif move_ == "L":
            self.direction += value
        else:  # F
            self.position += Vector.unit(self.direction) * value

    def move2(self, instruction):
        move_, value = parse_instruction(instruction)
        if move_ == "N":
            self.waypoint += Vector(0, value)
        elif move_ == "S":
            self.waypoint -= Vector(0, value)
        elif move_ == "E":
            self.waypoint += Vector(value, 0)
        elif move_ == "W":
            self.waypoint -= Vector(value, 0)
        elif move_ == "R":
            self.waypoint = self.waypoint.rotate(-value)
        elif move_ == "L":
            self.waypoint = self.waypoint.rotate(value)
        else:  # F
            self.position += self.waypoint * value

    def manhattan_distance(self):
        return int(round(abs(self.position.x) + abs(self.position.y)))


def answer(instructions, move_type=1):
    ship = Ship()
    [ship.move(instruction, move_type) for instruction in instructions]
    return ship.manhattan_distance()


def main():
    instructions = get_instructions("input.txt")
    assert answer(instructions, move_type=1) == 362
    assert answer(instructions, move_type=2) == 29895
    print("All tests passed.")


if __name__ == "__main__":
    main()
