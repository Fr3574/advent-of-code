"""
Advent of Code 2023, Day 11
"""
from itertools import combinations

def dists_sum(universe: list[list[str]], spacing: int) -> list[int]:
    empty_rows, empty_cols = [[idx for idx, line in enumerate(u) if '#' not in line] for u in (universe, zip(*universe))]
    galaxies = [(row, column) for row, line in enumerate(universe) for column, c in enumerate(line) if c == '#']
    galaxies = [(row + sum(er < row for er in empty_rows) * spacing, column + sum(ec < column for ec in empty_cols) * spacing) for (row, column) in galaxies]
    return sum(abs(x1 - x0) + abs(y1 - y0) for (x0, y0), (x1, y1) in combinations(galaxies, 2))

with open("input.txt", "r", encoding="utf-8") as f:
    universe = [list(line) for line in f.read().splitlines()]
    print(f"Solution 1 is: {dists_sum(universe, 1)}")
    print(f"Solution 2 is: {dists_sum(universe, 999_999)}")