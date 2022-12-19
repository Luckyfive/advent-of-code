#!/usr/bin/env python3
import os
import pathlib


def scoreRound(option1, option2):
    score = 0
    if option2 == "X":
        score += 1
    elif option2 == "Y":
        score += 2
    else:
        score += 3

    if option1 == "A":
        if option2 == "X":
            score += 3
        elif option2 == "Y":
            score += 6
        else:
            score += 0
    elif option1 == "B":
        if option2 == "X":
            score += 0
        elif option2 == "Y":
            score += 3
        else:
            score += 6
    else:
        if option2 == "X":
            score += 6
        elif option2 == "Y":
            score += 0
        else:
            score += 3
    return score


def scoreRound2(option1, option2):
    score = 0
    if option2 == "X":
        score += 0
    elif option2 == "Y":
        score += 3
    else:
        score += 6

    if option1 == "A":
        if option2 == "X":
            score += 3
        elif option2 == "Y":
            score += 1
        else:
            score += 2
    elif option1 == "B":
        if option2 == "X":
            score += 1
        elif option2 == "Y":
            score += 2
        else:
            score += 3
    else:
        if option2 == "X":
            score += 2
        elif option2 == "Y":
            score += 3
        else:
            score += 1
    return score


def partOne():
    """ Find score after using Rock/Paper/Scissor guide. """
    filePath = pathlib.Path(__file__).parent.resolve()

    totalScore = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            options = line.strip().split(' ')
            # print(options)
            totalScore += scoreRound(options[0], options[1])

    return totalScore


def partTwo():
    """ Find score after using Rock/Paper/Scissor guide. """
    filePath = pathlib.Path(__file__).parent.resolve()

    totalScore = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            options = line.strip().split(' ')
            # print(options)
            totalScore += scoreRound2(options[0], options[1])

    return totalScore


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
