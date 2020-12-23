#!/usr/bin/env python


EXAMPLE = [3, 8, 9, 1, 2, 5, 4, 6, 7]
INPUT = list(map(int, list("496138527")))


class LinkedList:
    def __init__(self, nodes):
        self.next = {node: next for node, next in zip(nodes, nodes[1:])}
        self.next[nodes[-1]] = nodes[0]
        self.n = len(self.next)

    def print(self, start):
        print(start)
        next = self.next[start]
        while True:
            print(next)
            next = self.next[next]
            if next == start:
                break

    def after_one(self):
        str_ = ""
        next = self.next[1]
        while True:
            str_ += str(next)
            next = self.next[next]
            if next == 1:
                break
        return str_

    def move(self, current):
        dest = current - 1
        if dest == 0:
            dest = self.n

        first = self.next[current]
        second = self.next[first]
        last = self.next[second]

        while dest in [first, second, last]:
            dest -= 1
            if dest == 0:
                dest = self.n

        self.next[current] = self.next[last]
        self.next[last] = self.next[dest]
        self.next[dest] = first
        return self.next[current]

    def moves(self, start, num_moves):
        next = start
        n = 0
        while n < num_moves:
            next = self.move(next)
            n += 1


def part1(sequence):
    ll = LinkedList(sequence)
    next = sequence[0]
    ll.moves(next, 100)
    return ll.after_one()


def part2(sequence):
    sequence.extend([i for i in range(max(sequence) + 1, 1000000 + 1)])
    ll = LinkedList(sequence)
    next = sequence[0]
    ll.moves(next, 10000000)
    first = ll.next[1]
    second = ll.next[first]
    return first * second


def main():
    assert part1(INPUT) == "69425837"
    assert part2(INPUT) == 218882971435
    print("All tests passed.")


if __name__ == "__main__":
    main()
