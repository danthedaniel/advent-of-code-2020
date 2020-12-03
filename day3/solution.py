#!/usr/bin/env python3

from functools import reduce

terrain = []

with open("input", "r") as file:
    for line in file.readlines():
        terrain.append([char == "#" for char in line.strip()])


def count_trees(right, down):
    trees_encountered = 0
    position = (0, 0)

    while True:
        if terrain[position[1]][position[0]]:
            trees_encountered += 1
        
        position = ((position[0] + right) % len(terrain[0]), position[1] + down)

        if position[1] >= len(terrain):
            return trees_encountered


print(f"Part 1: {count_trees(3, 1)}")

inputs = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
print(f"Part 2: {reduce(lambda acc, x: acc * x, [count_trees(*input) for input in inputs], 1)}")