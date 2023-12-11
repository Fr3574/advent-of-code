"""
Advent of Code 2023, Day 02
"""

from math import prod

LIMITATIONS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def is_game_possible(limitations: dict, sets: list[str]) -> bool:
    for s in sets:
        for pull in s.split(","):
            value, colour = pull.strip().split(" ")
            if int(value) > LIMITATIONS[colour]:
                return False
    return True

def get_set_power(sets: list[str]) -> int:
    fewest_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for s in sets:
        for pull in s.split(","):
            value, colour = pull.strip().split(" ")
            fewest_cubes[colour] = max(fewest_cubes[colour], int(value))
    return prod(fewest_cubes.values())

with open("input.txt", "r", encoding="utf-8") as f:
    id_sum = 0
    powers_sum = 0
    for line in f:
        game, sets = line.split(":")
        id_sum += int(game.split(" ")[1]) if is_game_possible(LIMITATIONS, sets.strip().split(";")) else 0
        powers_sum += get_set_power(sets.strip().split(";"))
    print(f"Solution 1 is: {id_sum}")
    print(f"Solution 2 is: {powers_sum}")
