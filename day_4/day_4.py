from typing import Iterable, Tuple


def get_range(s: str) -> Tuple[int, int]:
    vals = s.split("-")
    assert len(vals) == 2
    return int(vals[0]), int(vals[1])


def test_get_range():
    assert get_range("12-120") == (12, 120,)
    assert get_range("1-1") == (1, 1,)


class OverlapFinder:

    def find_full_contained_ranges(self, pairs: Iterable[str]) -> int:
        n_fully_contained = 0

        for pair in pairs:

            left, right = pair.strip().split(",")
            min_l, max_l = get_range(left)
            min_r, max_r = get_range(right)

            if self.rule(min_l, max_l, min_r, max_r):
                n_fully_contained += 1

        return n_fully_contained

    def rule(self, min_l, max_l, min_r, max_r):
        raise NotImplementedError


class Part1(OverlapFinder):
    def rule(self, min_l, max_l, min_r, max_r):
        """Both min & max from one is within other range."""
        return min_l >= min_r and max_l <= max_r or min_r >= min_l and max_r <= max_l


class Part2(OverlapFinder):
    def rule(self, min_l, max_l, min_r, max_r):
        """Only one boundary within other range."""
        return min_r <= min_l <= max_r or min_l <= min_r <= max_l


def test_find_full_contained_ranges(i):
    r = Part1().find_full_contained_ranges(i)
    print(r)
    assert r == 2


def test_find_some_contained_ranges(i):
    r = Part2().find_full_contained_ranges(i)
    print(r)
    assert r == 5


mock = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
12-13,3-7
12-19,3-12
6-6,4-6
2-6,4-8""".splitlines()

test_get_range()
test_find_full_contained_ranges(mock)
test_find_some_contained_ranges(mock)


with open("input.txt", "r") as file:
    res = Part2().find_full_contained_ranges(file)

print(f"result is: {res}")
