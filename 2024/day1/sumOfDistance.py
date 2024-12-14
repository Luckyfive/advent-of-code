#!/usr/bin/env python3
import os
import pathlib

def partOne():
    """ Find sum of distances between two lists of locations. """
    filePath = pathlib.Path(__file__).parent.resolve()
    

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()

        # Create two separate lists for each column
        column1 = []
        column2 = []

        # Iterate through each line and split the values
        for line in lines:
            col1, col2 = map(int, line.split())  # Convert to integers and split
            column1.append(col1)
            column2.append(col2)
    
    # Step 1: Sort both lists
    column1.sort()
    column2.sort()

    # Step 2: Calculate the differences and sum them up
    total_difference = sum(abs(a - b) for a, b in zip(column1, column2))
    return total_difference

def partTwo():
    """ Find sum of distances between two lists of locations. """
    filePath = pathlib.Path(__file__).parent.resolve()
    

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()

        # Create two separate lists for each column
        column1 = []
        column2 = []
        column2Dict = {}

        # Iterate through each line and split the values
        for line in lines:
            col1, col2 = map(int, line.split())  # Convert to integers and split
            column1.append(col1)
            column2.append(col2)
            
            if col2 in column2Dict:
                column2Dict[col2] = column2Dict[col2] + 1
            else:
                column2Dict[col2] = 1

    resultList = []
    for number in column1:
        if number in column2Dict:
            resultList.append(number * column2Dict[number])
        else:
            resultList.append(0)

    # Step 2: Calculate the differences and sum them up
    similarity_score = sum(resultList)
    return similarity_score

if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")