#!/usr/bin/env python3
import os
import pathlib


def partOne():
    """ Compare a list of numbers and count how many are bigger than the previous """
    filePath = pathlib.Path(__file__).parent.resolve()
    lastNum = 0
    increaseCount = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            currNum = int(line)
            if lastNum != 0:
                if currNum > lastNum:
                    increaseCount += 1
            lastNum = currNum
    return increaseCount


def sumOfArray(givenArray):
    sum = 0
    for i in givenArray:
        sum += i
    return sum


def partTwo():
    """ Compare measurement totals and count how many are bigger than the previous """
    filePath = pathlib.Path(__file__).parent.resolve()
    increaseCount = 0

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        index = 0
        lastSum = 0
        for line in lines:
            try:
                currArray = [int(line), int(
                    lines[index+1]), int(lines[index+2])]
                if lastSum == 0:
                    lastSum = sumOfArray(currArray)
                else:
                    currSum = sumOfArray(currArray)
                    if currSum > lastSum:
                        increaseCount += 1
                    lastSum = currSum
                index += 1
            except IndexError:
                continue
    return increaseCount


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
