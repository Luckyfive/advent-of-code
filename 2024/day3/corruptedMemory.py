#!/usr/bin/env python3
import os
import pathlib
import re

def partOne():
    """ Find sum of distances between two lists of locations. """
    filePath = pathlib.Path(__file__).parent.resolve()
    
    sum = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()

        # Iterate through each line and split the values
        for line in lines:
            p = re.compile('mul\((\d{1,3}),(\d{1,3})\)')
            m = p.findall(line)
            for pair in m:
                sum += int(pair[0]) * int(pair[1])

    return sum

def get_text_between_matches(pattern, text):
    matches = list(re.finditer(pattern, text))
    result = []
    
    for i in range(len(matches) - 1):
        start = matches[i].end()  # End of the current match
        end = matches[i + 1].start()  # Start of the next match
        result.append(text[start:end])
    
    return result

def partTwo():
    """ Find sum of distances between two lists of locations. """
    filePath = pathlib.Path(__file__).parent.resolve()
    
    sum = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()

        # Iterate through each line and split the values
        for line in lines:
            p = re.compile('mul\((\d{1,3}),(\d{1,3})\)')

            # get list of in between text
            text_between = get_text_between_matches(p, line)

            m = p.findall(line)

            for index, pair in enumerate(m):
                if index <= len(text_between) - 1:
                    if "don\'t" not in text_between[index]:
                        sum += int(pair[0]) * int(pair[1])

    return sum

if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")