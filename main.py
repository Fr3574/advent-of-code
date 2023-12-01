"""
Advent of Code 2023, Day 01
"""

# Map for Solution 1
map1 = {str(i):i for i in range(1,10)}

# Map for Solution 2
map2 = map1 | {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6, 
  "seven": 7, 
  "eight": 8, 
  "nine": 9,
}

def find_key_in_substring(s: str, mapping: dict, order = "first") -> int:
    for n in range(1, len(s) + 1):
        for key, value in mapping.items():
            if order == "first" and key in s[:n]:
                return value
            if order == "last" and key in s[-n:]:
                return value

with open("input.txt", "r", encoding="utf-8") as f:
    sol1, sol2 = 0, 0
    for line in f:
        sol1 += 10 * find_key_in_substring(line, map1) + find_key_in_substring(line, map1, order="last")
        sol2 += 10 * find_key_in_substring(line, map2) + find_key_in_substring(line, map2, order="last")
    print(f"Solution 1 is: {sol1}")
    print(f"Solution 2 is: {sol2}")
