#!/usr/bin/env python

from collections import defaultdict


def read_foods(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    return lines


def part1(foods):
    counts = defaultdict(int)
    intersections = defaultdict(list)

    for food in foods:
        ingredients, allergens = food.split("(contains ")
        ingredients = ingredients.strip().split()
        allergens = allergens.replace(")", "").replace(" ", "").split(",")
        for allergen in allergens:
            intersections[allergen].append(set(ingredients))
        for ingredient in ingredients:
            counts[ingredient] += 1

    contain_allergens = set.union(
        *[set.intersection(*v) for v in intersections.values()]
    )
    return sum(
        count
        for ingredient, count in counts.items()
        if ingredient not in contain_allergens
    )


def main():
    foods = read_foods("input.txt")
    assert part1(foods) == 2203
    print("All tests passed.")


if __name__ == "__main__":
    main()
