#!/usr/bin/env python


import copy


def read_input(path):
    with open(path) as f:
        player1, player2 = f.read().strip().split("\n\n")
    player1 = [int(x) for x in player1.split("\n")[1:]]
    player2 = [int(x) for x in player2.split("\n")[1:]]
    return player1, player2


def score(player):
    n = len(player)
    return sum([player[n - i] * i for i in reversed(range(1, n + 1))])


def part1(player1, player2):
    while player1 != [] and player2 != []:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
    if player1 == []:
        return score(player2)
    else:
        return score(player1)


def recursive_combat(player1, player2):

    seen = set()

    while player1 != [] and player2 != []:

        if tuple([tuple(player1), tuple(player2)]) in seen:
            return 1, player1
        seen.add(tuple([tuple(player1), tuple(player2)]))

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            winner, _ = recursive_combat(
                copy.copy(player1[:card1]), copy.copy(player2[:card2])
            )
        else:
            if card1 > card2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])

    if player1 == []:
        return 2, player2
    else:
        return 1, player1


def main():
    player1, player2 = read_input("input.txt")
    _, winning_cards = recursive_combat(player1, player2)
    assert score(winning_cards) == 36463
    print("All tests passed.")


if __name__ == "__main__":
    main()
