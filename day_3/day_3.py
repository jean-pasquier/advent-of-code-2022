from typing import Iterable


def split_half(s):
    half_size = int(len(s) / 2)
    return set(s[:half_size]), set(s[half_size:])


def test_split():
    r = split_half("abcddEFGHH")
    assert r == (set("abcd"), set("EFGH"))


def get_priority(char: str):
    return ord(char) - 96 if char.lower() == char else ord(char) - 38


def test_prio():
    assert get_priority("a") == 1
    assert get_priority("b") == 2
    assert get_priority("A") == 27
    assert get_priority("B") == 28
    assert get_priority("Z") == 52


def find_sum_priorities(rucksacks: Iterable[str]) -> int:
    priority = 0

    for ruck in rucksacks:
        c1, c2 = split_half(ruck)

        overlap = c1.intersection(c2)
        assert len(overlap) == 1
        item = overlap.pop()
        priority += get_priority(item)

    return priority


def test_find_sum_priorities(i):
    assert find_sum_priorities(i) == 157


def find_overlap(g: Iterable[set]) -> set:
    return set.intersection(*g)


def test_overlap():
    assert find_overlap([set("ABCC"), set("BCD"), set("CDE")]) == set("C")
    assert find_overlap([set("ABC"), set("BCD"), set("CDE")]) == set("C")


def find_badge_priority(rucksacks: Iterable[str]) -> int:
    priority = 0
    it = iter(rucksacks)

    while True:
        try:
            group = [set(next(it).strip()) for _ in range(3)]
        except StopIteration:
            break
        overlap = find_overlap(group)
        assert len(overlap) == 1
        item = overlap.pop()
        priority += get_priority(item)

    return priority


def test_find_badge_priority(i):
    r = find_badge_priority(i)
    print(r)
    assert r == 70


mock = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

test_prio()
test_split()
test_find_sum_priorities(mock)
test_overlap()
test_find_badge_priority(mock)

with open("input.txt", "r") as file:
    r = find_badge_priority(file)

print(f"result is : {r}")

