#!/usr/bin/env python3
import pathlib
import re
import math

def partOne():
    """ Given certain conditions, return how many lanternfish are there after 80 days."""
    filePath = pathlib.Path(__file__).parent.resolve()
    counts = []
    finalCount = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        counts = [int(num) for num in lines[0].split(',')]

        print(f"Initial State: {counts}")
        for day in range(1, 81):
            for index, currFish in enumerate(counts):
                if currFish == 0:
                    counts.append(9)
                    counts[index] = 6
                    continue
                counts[index] = currFish-1
    return len(counts)


def partTwo():
    """ Given certain conditions, return how many lanternfish are there after 256 days."""
    filePath = pathlib.Path(__file__).parent.resolve()
    counts = []
    finalCount = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        counts = [int(num) for num in lines[0].split(',')]

        # print(f"Initial State: {counts}")
        for day in range(1, 257):
            for index, currFish in enumerate(counts):
                if currFish == 0:
                    counts.append(9)
                    counts[index] = 6
                    continue
                counts[index] = currFish-1
    return len(counts)


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
