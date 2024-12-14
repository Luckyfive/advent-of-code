#!/usr/bin/env python3
import os
import pathlib

def partOne():
    """ Find sum of distances between two lists of locations. """
    filePath = pathlib.Path(__file__).parent.resolve()
    
    safe_report_count = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()

        # Iterate through each line and split the values
        for line in lines:
            try:
                currReport = [int(x) for x in line.split()]  # Convert each item to an integer
                result = check_rules(currReport)

                if result:
                    safe_report_count += 1
            except ValueError as e:
                print(f"Error converting line to integers: {line}. Skipping this line.")

    return safe_report_count

def check_rules(numbers):
    if len(numbers) < 2:
        return True  # A list with 0 or 1 element trivially satisfies the rules.
    
    # Check if the list is all increasing or all decreasing
    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
    
    if not (is_increasing or is_decreasing):
        return False
    
    # Check the difference condition
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < 1 or diff > 3:
            return False
    
    return True

def partTwo():
    """ Find sum of distances between two lists of locations. """
    filePath = pathlib.Path(__file__).parent.resolve()
    
    safe_report_count = 0
    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()

        # Iterate through each line and split the values
        for line in lines:
            try:
                currReport = [int(x) for x in line.split()]  # Convert each item to an integer

                # Check if the original list satisfies the rules
                if check_rules(currReport):
                    safe_report_count += 1
                    continue

                # Check if removing one number makes the list satisfy the rules
                for i in range(len(currReport)):
                    modified_list = currReport[:i] + currReport[i + 1:]  # Remove the i-th element
                    if check_rules(modified_list):
                        safe_report_count += 1
                        break

            except ValueError as e:
                print(f"Error converting line to integers: {line}. Skipping this line.")

    return safe_report_count

if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")