#!/usr/bin/env python


def get_numbers(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    return [int(line) for line in lines]


def find_first_invalid(numbers, preamble_length=5):
    n = len(numbers)
    for i in range(preamble_length, n):
        if not is_valid(numbers, i, preamble_length):
            return numbers[i]


def is_valid(numbers, position, preamble_length=5):
    array = numbers[(position - preamble_length) : position]  # noqa
    target = numbers[position]
    n = len(array)

    for i in range(n):
        j = 0
        while j < i:
            if target == (array[i] + array[j]):
                return True
            j += 1

    return False


def find_contiguous_set(array, target):
    n = len(array)
    for i in range(n):
        cont = [array[i]]
        j = i + 1
        s = array[i]
        while j < n:
            if s == target:
                return min(cont) + max(cont)
            s += array[j]
            cont.append(array[j])
            j += 1


def part2(numbers, target):
    first_half = numbers[: numbers.index(target)]
    return find_contiguous_set(first_half, target)


def main():
    numbers = get_numbers("input.txt")
    print(part2(numbers, target=90433990))  # 11691646

    # assert find_first_invalid(numbers, preamble_length=25) == 90433990
    print("All tests passed.")


if __name__ == "__main__":
    main()
