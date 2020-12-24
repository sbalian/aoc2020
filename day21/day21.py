#!/usr/bin/env python

from collections import defaultdict


def read_foods(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")

    foods = []
    counts = defaultdict(int)

    for line in lines:
        ingredients, allergens = line.split("(contains ")
        ingredients = ingredients.strip().split()
        allergens = allergens.replace(")", "").replace(" ", "").split(",")
        foods.append([ingredients, allergens])
        for ingredient in ingredients:
            counts[ingredient] += 1
    return foods, counts


def part1(foods, counts):
    intersections = defaultdict(list)
    for ingredients, allergens in foods:
        for allergen in allergens:
            intersections[allergen].append(set(ingredients))
    contain_allergens = set.union(
        *[set.intersection(*v) for v in intersections.values()]
    )
    return (
        sum(
            count
            for ingredient, count in counts.items()
            if ingredient not in contain_allergens
        ),
        contain_allergens,
    )


def resolve(allergens):
    for allergen, ingredients in allergens.items():
        if len(ingredients) == 1:
            resolved_ingredient = list(ingredients)[0]
            resolved_allergen = allergen
            break
    del allergens[resolved_allergen]
    for allergen, ingredients in allergens.items():
        if resolved_ingredient in ingredients:
            allergens[allergen].remove(resolved_ingredient)
    return allergens, resolved_allergen, resolved_ingredient


def part2(foods, counts):
    _, contain_allergens = part1(foods, counts)
    inerts = set(counts.keys() - contain_allergens)

    allergens = defaultdict(list)
    for ingredients, contains in foods:
        for allergen in contains:
            allergens[allergen].append(
                set(
                    [
                        ingredient
                        for ingredient in ingredients
                        if ingredient not in inerts
                    ]
                )
            )

    resolved = []
    allergens = {k: set.intersection(*v) for k, v in allergens.items()}
    while allergens != {}:
        allergens, allergen, ingredient = resolve(allergens)
        resolved.append((allergen, ingredient))

    return ",".join(
        [ingredient[1] for ingredient in sorted(resolved, key=lambda x: x[0])]
    )


def main():
    foods, counts = read_foods("input.txt")
    answer, _ = part1(foods, counts)
    assert answer == 2203
    assert (
        part2(foods, counts)
        == "fqfm,kxjttzg,ldm,mnzbc,zjmdst,ndvrq,fkjmz,kjkrm"
    )
    print("All tests passed.")


if __name__ == "__main__":
    main()
