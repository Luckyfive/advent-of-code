#!/usr/bin/env python3
from ast import Index
import os
import pathlib


class Board:
    def __init__(self, id):
        self.id = id
        self.rows = []
        self.columns = []
        self.rowScores = []
        self.columnScores = []
        self.winningIndex = None
        self.ignoreBoard = False
        self.winningNumbers = []

    def addRow(self, rowList):
        self.rows.append(rowList)

    def getRows(self):
        print(self.rows)

    def setColumns(self):
        for row in self.rows:
            for i in range(len(self.rows)):
                try:
                    self.columns[i].append(row[i])
                except IndexError:
                    self.columns.append([])
                    self.columns[i].append(row[i])

    def getColumns(self):
        if len(self.columns) == 0:
            self.setColumns()

        print(self.columns)

    def checkNumber(self, number, index):
        if len(self.columnScores) == 0:
            self.columnScores = [0] * len(self.columns)
        if len(self.rowScores) == 0:
            self.rowScores = [0] * len(self.rows)

        columnCounter = 0
        for column in self.columns:
            if number in column:
                self.columnScores[columnCounter] += 1
                if self.columnScores[columnCounter] == len(self.columns):
                    print("we've got a winner via columns!")
                    print(f"{index}")

                    if self.winningIndex == None:
                        self.winningIndex = index
                    else:
                        if index < self.winningIndex:
                            self.winningIndex = index
                    self.ignoreBoard = True

            columnCounter += 1

        rowCounter = 0
        for row in self.rows:
            if number in row:
                self.rowScores[rowCounter] += 1
                if self.rowScores[rowCounter] == 5:
                    print("we've got a winner via rows!")
                    print(f"{index}")

                    if self.winningIndex == None:
                        self.winningIndex = index
                    else:
                        if index < self.winningIndex:
                            self.winningIndex = index
                    self.ignoreBoard = True

                # print(
                #     f"board {self.id} contains this number: {number} with row: {row}")
            rowCounter += 1

    def getWinningNumbers(self):
        rowIndex = 0
        winningNumbers = {}
        for score in self.rowScores:
            if score != 5:
                rowIndex += 1
                continue
            else:
                winningNumbers = {num for num in self.rows[rowIndex]}

        colIndex = 0
        for score in self.columnScores:
            if score != 5:
                colIndex += 1
                continue
            else:
                winningNumbers = {num for num in self.columns[colIndex]}

        return list(winningNumbers)

    def getScores(self):
        print(f"rowScores: {self.rowScores}")
        print(f"columnScores: {self.columnScores}")
        print(f"winning index: {self.winningIndex}")
        print(f"board id: {self.id}")


def partOne():
    """ Use binary numbers to  calculate gamma and epsilon rates."""
    filePath = pathlib.Path(__file__).parent.resolve()
    winningNums = []
    boards = []

    with open(f'{filePath}/input.txt') as f:
        lines = f.readlines()
        lineCounter = 0
        boardCounter = 0
        for line in lines:
            line = line.strip('\n')
            if lineCounter == 0:
                winningNums = line.split(',')
                winningNums = [int(numeric_string)
                               for numeric_string in winningNums]
                print(winningNums)
            else:
                if line == '':
                    currentBoard = Board(boardCounter)
                    boards.append(currentBoard)
                    boardCounter += 1
                else:
                    line = line.split()
                    line = [int(numeric_string)
                            for numeric_string in line]
                    # print(line)
                    currentBoard.addRow(line)
            lineCounter += 1

        for index, number in enumerate(winningNums):
            for board in boards:
                board.setColumns()
                if board.ignoreBoard == False:
                    board.checkNumber(number, index)

        smallestIndex = None
        winningBoardId = None
        for board in boards:
            board.getScores()

            if board.winningIndex != None:
                print("we've got a winner board")
                if smallestIndex == None:
                    smallestIndex = board.winningIndex
                    winningBoardId = board.id
                elif board.winningIndex < smallestIndex:
                    smallestIndex = board.winningIndex
                    winningBoardId = board.id

        print(
            f"smallest index: {smallestIndex}; winning board: {winningBoardId}")

        unmarkedNums = []
        unmarkedSum = 0
        winningBoard = boards[winningBoardId]
        winningRows = winningBoard.rows
        for row in winningRows:
            for currNum in row:
                if currNum in winningNums[:winningBoard.winningIndex+1]:
                    continue
                else:
                    print(f"found number that is unmarked: {currNum}")
                    unmarkedNums.append(currNum)
                    unmarkedSum += currNum
        print(winningBoard.rows)
        print(unmarkedNums)
        print(winningNums[:winningBoard.winningIndex+1])
        print(winningBoard.getWinningNumbers())
        print(f"unmarked sum: {unmarkedSum}; unmarked nums: {unmarkedNums}")
        print(
            f"last number called: {winningNums[winningBoard.winningIndex]}")
        return unmarkedSum * winningNums[winningBoard.winningIndex]


def partTwo():
    """ Use readings to find a final number which is final horizontal multiplied by final depth.
    This time with different rules and a third variable called aim. """
    return None


if __name__ == "__main__":
    print(f"partOne: {partOne()}")
    print(f"partTwo: {partTwo()}")
