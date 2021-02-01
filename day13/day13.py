#!/usr/bin/env python


def part1(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    earliest = int(lines[0])
    ids = [int(x) for x in lines[1].split(",") if x != "x"]
    a = [(id, ((earliest // id) + 1) * id) for id in ids]
    min_ = min(a, key=lambda x: x[1])
    return (min_[1] - earliest) * min_[0]


def get_term(a, b, diff, d):
    i = 1
    while True:
        answer = a * i + d
        if (answer + diff) % b == 0:
            break
        else:
            i += 1
    first = answer
    i += 1
    while True:
        answer = a * i + d
        if (answer + diff) % b == 0:
            break
        else:
            i += 1
    second = answer
    d = second - first
    return first, d


def part2(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")

    buses = [
        (int(id), arrival)
        for arrival, id in enumerate([x for x in lines[1].split(",")])
        if id != "x"
    ]
    n = len(buses)
    first, d = get_term(buses[0][0], buses[1][0], buses[1][1], 0)
    for i in range(2, n):
        id_, arrival = buses[i]
        first, d = get_term(d, id_, arrival, first)
    return first


def main():
    assert part1("input.txt") == 3215
    # assert part2("example1.txt") == 1068781
    # assert part2("example2.txt") == 3417
    # assert part2("example3.txt") == 754018
    # assert part2("example4.txt") == 779210
    # assert part2("example5.txt") == 1261476
    # assert part2("example6.txt") == 1202161486
    assert part2("input.txt") == 1001569619313439

    print("All tests passed.")


if __name__ == "__main__":
    main()


# Graveyard
# passes all tests except for the input ... (does not seem to halt)
# def part2(path):
#     with open(path) as f:
#         lines = f.read().strip().split("\n")
#
#     buses = [
#         (int(id), arrival)
#         for arrival, id in enumerate([x for x in lines[1].split(",")])
#         if id != "x"
#     ]
#
#     answer = buses[0][0]
#     increment = buses[0][0]
#     n = len(buses)
#     # print(buses)
#
#     for i in range(1, n):
#         id_, arrival = buses[i]
#         while True:
#             if answer < id_:
#                 answer += increment
#                 continue
#             if answer % id_ == 0:
#                 answer += increment
#                 continue
#             if (((answer // id_) + 1) * id_ - answer) == arrival:
#                 increment *= id_  # likely mistake here
#                 break
#             else:
#                 answer += increment
#     return answer
