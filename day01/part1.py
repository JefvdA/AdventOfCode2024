#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest
from timeit import timeit


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    lines = s.split("\n")

    left = []
    right = []

    for line in lines:
        (a, b) = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    total_distance = 0
    for i in range(len(left)):
        left_distance = left[i]
        right_distance = right[i]
        distance_difference = abs(left_distance - right_distance)
        total_distance += distance_difference
    return total_distance


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""3   4
4   3
2   5
1   3
3   9
3   3""", 11),
        ("""34   40
42   32
20   80""", 56),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        ex_time = timeit(lambda: print(compute(f.read())), number=1)
    print(f"Execution time: {ex_time:.3f} seconds")


if __name__ == "__main__":
    main()