from typing import Iterable
from itertools import chain
import heapq

EMPTY_LINE = ""


def find_max_calories(raw_calories: Iterable[str]) -> int:
    max_cal = 0
    current_cal = 0

    for raw_line in raw_calories:

        line = raw_line.strip()

        # inside current elf paragraph
        if line != EMPTY_LINE:
            current_cal += int(line)
            continue

        # otherwise marking as max if current is higher
        if current_cal > max_cal:
            max_cal = current_cal

        # jumping to next paragraph
        current_cal = 0

    # handle last elf
    return max(current_cal, max_cal)


def test_find_max_calories(i):
    assert find_max_calories(i) == 6000


def find_top_calories(raw_calories: Iterable[str], n: int = 3) -> int:
    current_cal = 0
    top_calories = []

    for raw_line in chain(raw_calories, [EMPTY_LINE]):
        line = raw_line.strip()

        # inside current elf paragraph
        if line != EMPTY_LINE:
            current_cal += int(line)
            continue

        # otherwise: before jumping to next paragraph
        if len(top_calories) < n:
            heapq.heappush(top_calories, current_cal)
        else:
            heapq.heapreplace(top_calories, current_cal)

        current_cal = 0

    return sum(top_calories)


def test_find_top_calories(i):
    r = find_top_calories(i, 3)
    r2 = find_top_calories(i, 2)
    print(r)
    print(r2)
    assert r == 14000
    assert r2 == 11_000


if __name__ == "__main__":

    mock_input = """1000
    2000
    
    2000
    3000
    
    2500
    
    6000""".splitlines()
    print(f"testing with {mock_input}")

    test_find_max_calories(mock_input)
    test_find_top_calories(mock_input)

    with open("input.txt", "r") as file:
        result = find_top_calories(file, 3)

    print(f"result: {result}")
