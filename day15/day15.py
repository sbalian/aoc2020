#!/usr/bin/env python


from collections import defaultdict


def brute_force(starting_numbers, n):
    n += 1
    spoken = defaultdict(list)
    for i, starting_number in enumerate(starting_numbers):
        spoken[starting_number].append(i + 1)
        last_number_spoken = starting_number

    for i in range(i + 2, n):
        if len(spoken[last_number_spoken]) == 1:
            number_spoken = 0
        else:
            last = spoken[last_number_spoken][-1]
            right_before_last = spoken[last_number_spoken][-2]
            number_spoken = last - right_before_last

        if len(spoken[number_spoken]) == 2:
            spoken[number_spoken].pop(0)
        spoken[number_spoken].append(i)

        last_number_spoken = number_spoken
    return last_number_spoken


def main():
    starting_numbers = [18, 11, 9, 0, 5, 1]
    assert brute_force(starting_numbers, 2020) == 959
    assert brute_force(starting_numbers, 30000000) == 116590
    print("All tests passed.")


if __name__ == "__main__":
    main()


# Alternative to see if there is speedup ... answer, no!
# class Pair:
#     def __init__(self):
#         self.first = None
#         self.second = None
#
#     def get_difference(self):
#         return self.second - self.first
#
#     def add(self, value):
#         if self.first is None and self.second is None:
#             self.first = value
#         elif self.first is not None and self.second is None:
#             self.second = value
#         else:
#             self.first = self.second
#             self.second = value
#
#
# def brute_force(starting_numbers, n):
#     n += 1
#     spoken = defaultdict(Pair)
#     for i, starting_number in enumerate(starting_numbers):
#         spoken[starting_number].add(i + 1)
#         last_number_spoken = starting_number
#
#     for i in range(i + 2, n):
#         if spoken[last_number_spoken].second is None:
#             number_spoken = 0
#         else:
#             number_spoken = spoken[last_number_spoken].get_difference()
#
#         spoken[number_spoken].add(i)
#         last_number_spoken = number_spoken
#     return last_number_spoken
