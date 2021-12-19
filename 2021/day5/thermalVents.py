#!/usr/bin/env python3
import pathlib
import re


def partOne():
    """ Given vectors, find how many points have major overlap. """
    filePath = pathlib.Path(__file__).parent.resolve()
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            pattern = re.compile(
                "(?P<x1>\d+)\,(?P<y1>\d+)\s+->\s+(?P<x2>\d+)\,(?P<y2>\d+)")
            match = pattern.search(line)
            x1 = int(match.group("x1"))
            y1 = int(match.group("y1"))
            x2 = int(match.group("x2"))
            y2 = int(match.group("y2"))
            print(f'x1 {x1} y1 {y1} x2 {x2} y2 {y2}')
            if x1 == x2 or y1 == y2:
                print("not skipped!")
            else:
                print("skipped!")
    return None


def partTwo():
    """ None. """
    return None


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
