#!/usr/bin/env python


def get_expense_report(path):
    with open(path) as f:
        return [int(e) for e in f.read().strip().split()]


def pairs(er, target):
    for i in range(len(er)):
        j = 0
        while j < i:
            if (er[i] + er[j]) == target:
                return er[i] * er[j]
            j += 1


def triplets(er, target):
    for i in range(len(er)):
        j = 0
        while j < i:
            k = 0
            while k < j:
                if (er[i] + er[j] + er[k]) == target:
                    return er[i] * er[j] * er[k]
                k += 1
            j += 1


def main():
    er = get_expense_report("input.txt")
    assert pairs(er, 2020) == 878724
    assert triplets(er, 2020) == 201251610
    print("All tests passed.")


if __name__ == "__main__":
    main()
