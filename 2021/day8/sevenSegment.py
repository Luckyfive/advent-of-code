#!/usr/bin/env python3
import pathlib


def partOne():
    """ Given seven segment signals, return how many times 1, 4, 7, 8 show up."""
    filePath = pathlib.Path(__file__).parent.resolve()
    finalCounts = [0] * 9

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split('|')
            outputList = parts[1].split()
            for segment in outputList:
                length = len(segment)
                if length == 2:
                    finalCounts[1] += 1
                elif length == 4:
                    finalCounts[4] += 1
                elif length == 3:
                    finalCounts[7] += 1
                elif length == 7:
                    finalCounts[8] += 1
        
        result = sum(finalCounts)

    return result

def partTwo():
    """ Given seven segment signals, return how many times 1, 4, 7, 8 show up."""
    filePath = pathlib.Path(__file__).parent.resolve()

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
    return None

if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
