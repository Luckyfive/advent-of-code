#!/usr/bin/env python3
import pathlib
import re
import math

def partOne():
    """ Given vectors, find how many points have major overlap. Only vertical and horizontal lines."""
    filePath = pathlib.Path(__file__).parent.resolve()
    finalPointMap = {}
    finalCount = 0
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

            if x1 == x2:
                difference = y1 - y2
                currStep = 1
                if difference < 0:
                    currStep = -1
                for diff in range(0, y1-(y2-currStep), currStep):
                    currY = y1-diff
                    coordinate = f"{x1},{currY}"
                    if coordinate not in finalPointMap:
                        finalPointMap[coordinate] = 1
                    else:
                        currentValue = finalPointMap.get(coordinate)
                        finalPointMap[coordinate] = currentValue + 1
            elif y1 == y2:
                difference = x1 - x2
                currStep = 1
                if difference < 0:
                    currStep = -1
                for diff in range(0, x1-(x2-currStep), currStep):
                    currX = x1-diff
                    coordinate = f"{currX},{y1}"
                    if coordinate not in finalPointMap:
                        finalPointMap[coordinate] = 1
                    else:
                        currentValue = finalPointMap.get(coordinate)
                        finalPointMap[coordinate] = currentValue + 1
            else:
                continue
        
        for key, value in finalPointMap.items():
            if value >= 2:
                finalCount += 1
    return finalCount


def partTwo():
    """ Given vectors, find how many points have major overlap. Vertical, Horizontal, and diagonal lines."""
    filePath = pathlib.Path(__file__).parent.resolve()
    finalPointMap = {}
    finalCount = 0
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

            if x1 == x2:
                difference = y1 - y2
                currStep = 1
                if difference < 0:
                    currStep = -1
                for diff in range(0, y1-(y2-currStep), currStep):
                    currY = y1-diff
                    coordinate = f"{x1},{currY}"
                    if coordinate not in finalPointMap:
                        finalPointMap[coordinate] = 1
                    else:
                        currentValue = finalPointMap.get(coordinate)
                        finalPointMap[coordinate] = currentValue + 1
            elif y1 == y2:
                difference = x1 - x2
                currStep = 1
                if difference < 0:
                    currStep = -1
                for diff in range(0, x1-(x2-currStep), currStep):
                    currX = x1-diff
                    coordinate = f"{currX},{y1}"
                    if coordinate not in finalPointMap:
                        finalPointMap[coordinate] = 1
                    else:
                        currentValue = finalPointMap.get(coordinate)
                        finalPointMap[coordinate] = currentValue + 1
            else:
                deltaY = y2-y1;
                deltaX = x2-x1;
                angle = math.degrees(math.atan2(deltaY, deltaX)); 
                if angle == 45:
                    difference = x1 - x2
                    currStep = 1
                    if difference < 0:
                        currStep = -1
                    for diff in range(0, x1-(x2-currStep), currStep):
                        currX = x1-diff
                        currY = y1-diff
                        coordinate = f"{currX},{currY}"
                        if coordinate not in finalPointMap:
                            finalPointMap[coordinate] = 1
                        else:
                            currentValue = finalPointMap.get(coordinate)
                            finalPointMap[coordinate] = currentValue + 1
                elif angle == -45:
                    difference = x1 - x2
                    currStep = 1
                    if difference < 0:
                        currStep = -1
                    for diff in range(0, x1-(x2-currStep), currStep):
                        currX = x1-diff
                        currY = y1+diff
                        coordinate = f"{currX},{currY}"
                        if coordinate not in finalPointMap:
                            finalPointMap[coordinate] = 1
                        else:
                            currentValue = finalPointMap.get(coordinate)
                            finalPointMap[coordinate] = currentValue + 1
                elif angle == 135:
                    difference = x1 - x2
                    currStep = 1
                    if difference < 0:
                        currStep = -1
                    for diff in range(0, x1-(x2-currStep), currStep):
                        currX = x1-diff
                        currY = y1+diff
                        coordinate = f"{currX},{currY}"
                        if coordinate not in finalPointMap:
                            finalPointMap[coordinate] = 1
                        else:
                            currentValue = finalPointMap.get(coordinate)
                            finalPointMap[coordinate] = currentValue + 1
                elif angle == -135:
                    difference = x1 - x2
                    currStep = 1
                    if difference < 0:
                        currStep = -1
                    for diff in range(0, x1-(x2-currStep), currStep):
                        currX = x1-diff
                        currY = y1-diff
                        coordinate = f"{currX},{currY}"
                        if coordinate not in finalPointMap:
                            finalPointMap[coordinate] = 1
                        else:
                            currentValue = finalPointMap.get(coordinate)
                            finalPointMap[coordinate] = currentValue + 1
                else:
                    continue

        
        for key, value in finalPointMap.items():
            if value >= 2:
                finalCount += 1
    return finalCount


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
