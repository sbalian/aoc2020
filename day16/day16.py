#!/usr/bin/env python

import functools


def get_allowed_values(string_range):
    min_, max_ = map(int, string_range.split("-"))
    return set(i for i in range(min_, max_ + 1))


def read_notes(path):
    with open(path) as f:
        notes = f.read().strip().split("\n\n")

    rules, my_ticket, nearby_tickets = notes
    rules = rules.split("\n")

    allowed = {}
    for rule in rules:
        key, values = rule.split(": ")
        first_range, second_range = values.split(" or ")
        allowed[key] = get_allowed_values(first_range).union(
            get_allowed_values(second_range)
        )

    my_ticket = [int(x) for x in my_ticket.split("\n")[1].split(",")]

    nearby_tickets = [
        [int(x) for x in ticket.split(",")]
        for ticket in nearby_tickets.split("\n")[1:]
    ]

    return allowed, my_ticket, nearby_tickets


def find_invalid_tickets(allowed, nearby_tickets):
    invalid_values = []
    invalid_ids = []
    all_allowed = set.union(*allowed.values())

    for i, nearby_ticket in enumerate(nearby_tickets):
        not_allowed = list(set(nearby_ticket) - all_allowed)
        if not_allowed != []:
            invalid_ids.append(i)
        invalid_values.extend(not_allowed)

    return invalid_ids, sum(invalid_values)


def departure_products(allowed, nearby_tickets, my_ticket, invalid_ids):
    nearby_tickets = [
        nearby_ticket
        for i, nearby_ticket in enumerate(nearby_tickets)
        if i not in invalid_ids
    ]

    n_cols = len(nearby_tickets[0])
    n_tickets = len(nearby_tickets)

    candidates = {key: [i for i in range(n_cols)] for key in allowed}

    for i in range(n_cols):
        values = set([nearby_tickets[j][i] for j in range(n_tickets)])
        for key, allowed_ in allowed.items():
            if not values.issubset(allowed_):
                candidates[key].pop(candidates[key].index(i))

    mapping = {}
    for i in range(n_cols):
        matched_candidate, column, candidates = _find(candidates)
        mapping[matched_candidate] = column

    assert candidates == {}

    return functools.reduce(
        lambda x, y: x * y,
        [
            my_ticket[index]
            for key, index in mapping.items()
            if key.startswith("departure")
        ],
    )


def _find(candidates):
    for candidate, allowed in candidates.items():
        if len(allowed) == 1:
            column = allowed[0]
            matched_candidate = candidate
            break
    del candidates[matched_candidate]

    for candidate, allowed in candidates.items():
        if column in allowed:
            candidates[candidate].remove(column)

    return matched_candidate, column, candidates


def main():
    allowed, my_ticket, nearby_tickets = read_notes("input.txt")
    invalid_ids, sum_invalid = find_invalid_tickets(allowed, nearby_tickets)
    assert sum_invalid == 21071
    assert (
        departure_products(allowed, nearby_tickets, my_ticket, invalid_ids)
        == 3429967441937
    )
    print("All tests passed.")


if __name__ == "__main__":
    main()
