#!/usr/bin/env python3
import pathlib
import re
import math

def partOne():
    """ Given certain conditions, return how many lanternfish are there after 80 days."""
    filePath = pathlib.Path(__file__).parent.resolve()
    finalCounts = [0] * 9;

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        counts = [int(num) for num in lines[0].split(',')]

        for fish in counts:
            finalCounts[fish] += 1

        for day in range(1, 81):
            spawned = 0

            for index, fish in enumerate(finalCounts):
                if index == 0:
                    spawned = finalCounts[0]
                else:
                    finalCounts[index-1] = finalCounts[index]
                
                finalCounts[index] = 0
            
            finalCounts[6] += spawned
            finalCounts[8] = spawned

        result = 0
        for currCount in finalCounts:
            result += currCount
    return result


def partTwo():
    """ Given certain conditions, return how many lanternfish are there after 256 days."""
    filePath = pathlib.Path(__file__).parent.resolve()
    finalCounts = [0] * 9;

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        counts = [int(num) for num in lines[0].split(',')]

        for fish in counts:
            finalCounts[fish] += 1

        for day in range(1, 257):
            spawned = 0

            for index, fish in enumerate(finalCounts):
                if index == 0:
                    spawned = finalCounts[0]
                else:
                    finalCounts[index-1] = finalCounts[index]
                
                finalCounts[index] = 0
            
            finalCounts[6] += spawned
            finalCounts[8] = spawned

        result = 0
        for currCount in finalCounts:
            result += currCount
    return result

if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
