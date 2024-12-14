#!/usr/bin/env python3
import os
import pathlib

def getPriority(common_character:str):
    if common_character.isupper():
        priority = ord(common_character) - 38
        # print(priority)
    else:
        priority = ord(common_character) - 96
        # print(priority)

    return priority

def partOne():
    """ Find the sum of the priorities between two compartments. """
    filePath = pathlib.Path(__file__).parent.resolve()

    total_priority = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            middle = int(len(line.strip())/2)
            first_compartment = line[:middle]
            second_compartment = line[middle:]
            a=list(set(first_compartment)&set(second_compartment))
            total_priority += getPriority(a[0])
    # print(line)
    # print(first_compartment)
    # print(second_compartment)
    # print(a)
    # getPriority(a[0])
    # print(total_priority)
    return total_priority

def partTwo():
    """ Find the sum of the priorities between two compartments. """
    filePath = pathlib.Path(__file__).parent.resolve()

    total_priority = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        current_lines = []
        for line in lines:
            if len(current_lines) == 3:
                a=list(set(current_lines[0])&set(current_lines[1])&set(current_lines[2]))
                print(current_lines, a)
                total_priority += getPriority(a[0])
                current_lines = []
            else:
                current_lines.append(line.strip())
    # print(line)
    # print(first_compartment)
    # print(second_compartment)
    # print(a)
    # getPriority(a[0])
    # print(total_priority)
    return total_priority

if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
