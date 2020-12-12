#!/usr/bin/env python


def get_input(path):
    with open(path) as f:
        return [int(x) for x in f.read().strip().split("\n")]


def part1(adapters):
    adapters.sort()
    diffs = [y - x for x, y in zip(adapters, adapters[1:])]
    diffs.append(3)
    diffs.append(adapters[0])
    return diffs.count(1) * diffs.count(3)


def tribo(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribo(n - 3) + tribo(n - 2) + tribo(n - 1)


def part2(adapters):
    full_sequence = [0] + sorted(adapters) + [max(adapters) + 3]
    diffs = [y - x for x, y in zip(full_sequence, full_sequence[1:])]
    diffs = [str(x) for x in diffs]
    diffs = "".join(diffs).split("3")
    diffs = [len(x) for x in diffs if x not in ["", "1"]]
    prod = 1
    for diff in diffs:
        prod *= tribo(diff + 2)
    return prod


def main():
    adapters = get_input("input.txt")
    assert part1(adapters) == 3000
    assert part2(adapters) == 193434623148032
    print("All tests passed.")


if __name__ == "__main__":
    main()
