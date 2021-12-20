#!/usr/bin/env python3
import pathlib


def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def partOne():
    """ Use binary numbers to  calculate gamma and epsilon rates."""
    filePath = pathlib.Path(__file__).parent.resolve()
    result = []
    gamma = []
    epsilon = []

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            column = 0
            for bit in line:
                try:
                    result[column][int(bit)] += 1
                except IndexError:
                    result.append([0, 0])
                    result[column][int(bit)] += 1
                column += 1

    for first, second in result:
        if first > second:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

    gammaStr = ''.join(gamma)
    epsilonStr = ''.join(epsilon)

    finalResult = binaryToDecimal(
        int(gammaStr)) * binaryToDecimal(int(epsilonStr))
    return finalResult


def partTwo():
    """ Use readings to find a final number which is final horizontal multiplied by final depth.
    This time with different rules and a third variable called aim. """
    filePath = pathlib.Path(__file__).parent.resolve()
    oxygenRating = 0
    co2Rating = 0

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        currLines = lines[:]
        column = 0
        while len(currLines) > 1:
            bitCount = [0, 0]
            leftRightList = [[], []]
            for line in currLines:
                line = line.strip('\n')
                currBit = line[column]

                if currBit == '0':
                    bitCount[0] += 1
                    leftRightList[0].append(line)
                else:
                    bitCount[1] += 1
                    leftRightList[1].append(line)
            column += 1

            if bitCount[0] > bitCount[1]:
                currLines = leftRightList[0]
            else:
                currLines = leftRightList[1]
        oxygenRating = binaryToDecimal(int(currLines[0]))

        currLines = lines[:]
        column = 0
        while len(currLines) > 1:
            bitCount = [0, 0]
            leftRightList = [[], []]
            for line in currLines:
                line = line.strip('\n')
                currBit = line[column]

                if currBit == '0':
                    bitCount[0] += 1
                    leftRightList[0].append(line)
                else:
                    bitCount[1] += 1
                    leftRightList[1].append(line)
            column += 1

            if bitCount[0] > bitCount[1]:
                currLines = leftRightList[1]
            else:
                currLines = leftRightList[0]

        co2Rating = binaryToDecimal(int(currLines[0]))
    result = oxygenRating * co2Rating
    return result


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
