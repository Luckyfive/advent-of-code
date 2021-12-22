#!/usr/bin/env python3
import pathlib


def partOne():
    """ Given seven segment signals, return how many times 1, 4, 7, 8 show up."""
    filePath = pathlib.Path(__file__).parent.resolve()
    finalCounts = [0] * 10

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
    result = 0
    numSegments = [0] * 10

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            numSegments = [0] * 10
            parts = line.split('|')

            # figure out number segments
            guideList = parts[0].split()
            guideList.sort(key=len)

            for index, seg in enumerate(guideList):
                guideList[index] = "".join(sorted(seg))
            
            # save 7 and 8
            numSegments[7] = guideList[1]
            numSegments[8] = guideList[9]

            # figure out 1 and 4
            numSegments[1] = numberOne = guideList[0]
            numSegments[4] = numberFour = guideList[2]

            # figure out 2 missing letters (diff)
            numberOneSet = set(numberOne)
            numberFourSet = set(numberFour)
            difference = numberFourSet.symmetric_difference(numberOneSet)
            difference = "".join(list(sorted(difference)))

            numberFive = None
            # find len(5) with diff letters - this is number 5
            for index in range(3,6):
                if difference[0] in guideList[index] and difference[1] in guideList[index]:
                    numSegments[5] = numberFive = guideList[index]
    
            # find len(5) with letters from numberOne - this is number 3; other is number 2
            numberThree = None
            for index in range(3,6):
                if guideList[index] == numberFive:
                    continue
                elif numberOne[0] in guideList[index] and numberOne[1] in guideList[index]:
                    numSegments[3] = numberThree = guideList[index]
                else:
                    numSegments[2] = numberTwo = guideList[index]

            # find len(6) with one of diff letters missing - this is number 0
            for index in range(6,9):
                if difference[0] not in guideList[index] or difference[1] not in guideList[index]:
                    numSegments[0] = numberZero = guideList[index]

            # find len(6) with both letters from numberOne - this is number 9; other number is 6
            for index in range(6,9):
                if guideList[index] == numberZero:
                    continue
                elif numberOne[0] in guideList[index] and numberOne[1] in guideList[index]:
                    numSegments[9] = numberNine = guideList[index]
                else:
                    numSegments[6] = numberSix = guideList[index]

            outputList = parts[1].split()
            currentNumber = ""
            for segment in outputList:
                segment = "".join(sorted(segment))
                currentNumber += str(numSegments.index(segment))
            
            result += int(currentNumber)

    return result

if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
