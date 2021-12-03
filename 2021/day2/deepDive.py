#!/usr/bin/env python3
import os
import pathlib


def partOne():
    """ Use readings to find a final number which is final horizontal multiplied by final depth """
    filePath = pathlib.Path(__file__).parent.resolve()
    depth = 0
    horizontal = 0
    result = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            depthInfo = line.strip('\n').split(' ')
            direction = depthInfo[0]
            amount = int(depthInfo[1])

            if direction == 'forward':
                horizontal += amount
            elif direction == 'up':
                depth -= amount
            elif direction == 'down':
                depth += amount
            else:
                print("unknown direction")
        result = depth * horizontal
    return result


def partTwo():
    """ Use readings to find a final number which is final horizontal multiplied by final depth.
    This time with different rules and a third variable called aim. """
    filePath = pathlib.Path(__file__).parent.resolve()
    depth = 0
    horizontal = 0
    aim = 0
    result = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            depthInfo = line.strip('\n').split(' ')
            direction = depthInfo[0]
            amount = int(depthInfo[1])

            if direction == 'forward':
                horizontal += amount
                depth += aim * amount
            elif direction == 'up':
                aim -= amount
            elif direction == 'down':
                aim += amount
            else:
                print("unknown direction")
        result = depth * horizontal
    return result


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
