from typing import Iterable
from enum import Enum


class RPS(Enum):
    A = "Rock"
    B = "Paper"
    C = "Scissors"


# X defeats C
DEFEAT_RULES = {
    "X": RPS.C,
    "Y": RPS.A,
    "Z": RPS.B
}
# C is defeated by X
DEFEAT_BY_RULES = {v.name: k for k, v in DEFEAT_RULES.items()}

# match opponent to you and reverse
CORRESPONDING = {"X": "A", "Y": "B", "Z": "C"}
REVERSE_CORRESPONDING = {v: k for k, v in CORRESPONDING.items()}


SCORE_RULE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


class WinScore(Enum):
    win = 6
    draw = 3
    lose = 0


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
NEW_RULE = {
    "X": WinScore.lose,
    "Y": WinScore.draw,
    "Z": WinScore.win
}


def solve(strategy: Iterable[str]) -> int:

    score = 0

    for game in strategy:
        opponent, you = game.strip().split(" ")

        score += SCORE_RULE[you]

        if opponent == DEFEAT_RULES[you].name:
            score += WinScore.win.value
        elif opponent == CORRESPONDING[you]:
            score += WinScore.draw.value
        else:
            score += WinScore.lose.value

    return score


def test_solve(i):
    r = solve(i)
    assert r == 15


def solve_new_strategy(strategy: Iterable[str]) -> int:
    score = 0

    for game in strategy:
        opponent, ending = game.strip().split(" ")
        how = NEW_RULE[ending]

        if how == WinScore.lose:
            # is defeated by
            you = REVERSE_CORRESPONDING[DEFEAT_RULES[REVERSE_CORRESPONDING[opponent]].name]
        elif how == WinScore.draw:
            # reverse corresponding
            you = REVERSE_CORRESPONDING[opponent]
        else:
            # find you wining
            you = DEFEAT_BY_RULES[opponent]

        score += SCORE_RULE[you]
        score += how.value

    return score


def test_solve_new_strategy(i):
    r1 = solve_new_strategy(i)
    print(r1)
    assert r1 == 12


if __name__ == "__main__":

    mock_input = """A Y
B X
C Z""".splitlines()

    test_solve(mock_input)
    test_solve_new_strategy(mock_input)

    with open("input.txt", "r") as file:
        r = solve_new_strategy(file)
    print(f"result is: {r}")