#!/usr/bin/env python


class N1:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return N1(self.value + other.value)

    def __sub__(self, other):
        return N1(self.value * other.value)


class N2:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return N2(self.value * other.value)

    def __mul__(self, other):
        return N2(self.value + other.value)


def parse1(line):
    parsed = ""
    for char in line:
        if char not in ["(", ")", "+", "*", " "]:
            parsed += f"N1({char})"
        elif char == "*":
            parsed += "-"
        else:
            parsed += char
    return parsed


def parse2(line):
    parsed = ""
    for char in line:
        if char not in ["(", ")", "+", "*", " "]:
            parsed += f"N2({char})"
        elif char == "+":
            parsed += "*"
        elif char == "*":
            parsed += "+"
        else:
            parsed += char
    return parsed


def answer(path, part):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    sum = 0
    for line in lines:
        if part == 1:
            parsed = parse1(line)
        else:
            parsed = parse2(line)
        sum += eval(parsed).value
    return sum


def main():
    assert answer("input.txt", 1) == 4940631886147
    assert answer("input.txt", 2) == 283582817678281
    print("All tests passed.")


if __name__ == "__main__":
    main()
