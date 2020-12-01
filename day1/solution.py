#!/usr/bin/env python3

from itertools import product
from functools import reduce


def parse_input(path):
    expenses = []

    with open(path, "r") as input:
        for line in input.readlines():
            expenses.append(int(line))

    return expenses


def subset_sum(full_set, subset_size, target_sum):
    for subset in product(*[full_set] * subset_size):
        if sum(subset) == target_sum:
            return reduce(lambda acc, x: acc * x, subset, 1)


def main():
    target_sum = 2020
    expenses = parse_input("input")
    print(f"Part 1: {subset_sum(expenses, 2, target_sum)}")
    print(f"Part 2: {subset_sum(expenses, 3, target_sum)}")


if __name__ == "__main__":
    main()
