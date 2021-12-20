#!/usr/bin/env python3
import pathlib
import statistics


def partOne():
    """ Given positions, get the best fuel usage accounting for only horizontal movement."""
    filePath = pathlib.Path(__file__).parent.resolve()

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        positions = [int(num) for num in lines[0].split(',')]
        med = int(statistics.median(positions))
        fuelCount = 0

        for pos in positions:
            fuelCount += abs(pos-med)

    return fuelCount


def partTwo():
    """ Given positions, get the best fuel usage accounting for only horizontal movement and non-linear usage."""
    filePath = pathlib.Path(__file__).parent.resolve()

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        positions = [int(num) for num in lines[0].split(',')]
        meanNum = int(statistics.mean(positions))
        fuelCount = 0

        for pos in positions:
            currNum = abs(pos-meanNum)
            fuelCount += (currNum * (currNum + 1)) / 2

    return int(fuelCount)


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
