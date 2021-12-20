#!/usr/bin/env python3
import pathlib


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


def partOne():
    """ Given positions, get the best fuel usage accounting for only horizontal movement."""
    filePath = pathlib.Path(__file__).parent.resolve()

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        positions = [int(num) for num in lines[0].split(',')]
        med = int(median(positions))
        fuelCount = 0

        for pos in positions:
            fuelCount += abs(pos-med)

    return fuelCount


def partTwo():
    """ Given certain conditions, return how many lanternfish are there after 256 days."""
    filePath = pathlib.Path(__file__).parent.resolve()
    finalCounts = [0] * 9

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        counts = [int(num) for num in lines[0].split(',')]

    return None


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
