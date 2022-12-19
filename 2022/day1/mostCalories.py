#!/usr/bin/env python3
import os
import pathlib


def partOne():
    """ Find which elf is carrying the most calories. """
    filePath = pathlib.Path(__file__).parent.resolve()
    maxCalories = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        currentCalories = 0
        for line in lines:
            if len(line.strip()) > 0:
                currentCalories += int(line)
            else:
                if maxCalories < currentCalories:
                    # print(
                    #     f'maxCalories set to {currentCalories} from {maxCalories}')
                    maxCalories = currentCalories
                currentCalories = 0

    return maxCalories


def partTwo():
    """ Get total of top 3 calorie elves. """
    filePath = pathlib.Path(__file__).parent.resolve()
    maxCalories = 0
    topElves = []
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        currentCalories = 0
        for line in lines:
            if len(line.strip()) > 0:
                currentCalories += int(line)
            else:
                topElves.append(currentCalories)
                if maxCalories < currentCalories:
                    # print(
                    #     f'maxCalories set to {currentCalories} from {maxCalories}')
                    maxCalories = currentCalories
                currentCalories = 0

    # print(topElves)
    topElves.sort(reverse=True)
    # print(topElves)
    result = topElves[0] + topElves[1] + topElves[2]
    return result


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
