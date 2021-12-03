#!/usr/bin/env python3
from ast import Index
import os
import pathlib


def binaryToDecimal(binary):

    binary1 = binary
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
    print(gammaStr)
    print(epsilonStr)

    finalResult = binaryToDecimal(
        int(gammaStr)) * binaryToDecimal(int(epsilonStr))
    return finalResult


def partTwo():
    """ Use readings to find a final number which is final horizontal multiplied by final depth.
    This time with different rules and a third variable called aim. """
    filePath = pathlib.Path(__file__).parent.resolve()
    return None


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
