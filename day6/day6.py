#!/usr/bin/env python


def main():
    assert (
        sum(
            len(set(answer.replace("\n", "")))
            for answer in open("input.txt").read().strip().split("\n\n")
        )
        == 6249
    )
    assert (
        sum(
            len(set.intersection(*tuple(set(x) for x in answer.split("\n"))))
            for answer in open("input.txt").read().strip().split("\n\n")
        )
        == 3103
    )
    print("All tests passed.")


if __name__ == "__main__":
    main()
