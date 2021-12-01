#!/usr/bin/env python3
import os
import pathlib


def partOne():
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
    print(increaseCount)


if __name__ == "__main__":
    partOne()
