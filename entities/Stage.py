import tkinter
from math import ceil
from typing import Union, List

from entities.Point import Point
from entities.Row import Row


class Stage:
    def __init__(self, goal: int = 500, rowCount: int = 13, colCount: int = 9, numberRequestAmount: int = 5,
                 stageNumber: int = 1):
        self.goal = goal or 500
        self.rowCount = rowCount or 13
        self.colCount = colCount or 9
        self.rows: List[Union[Row, None]] = []
        self.numberRequestAmount = numberRequestAmount or 5
        self.stageNumber = stageNumber or 1

    def get(self, row: int, col: int):
        return self.rows[row].get(col)

    def requestMoreNumbers(self):
        # Get a list of all currently playable numbers from all rows
        # Make it a generator, so we consume it as we iterate
        playableNumbers = (number for row in self.rows for number in row.getPlayableNumbers())

        # Get last position of the last row
        startRow = self.rows[-1]
        startCol = len(startRow.numbers) - 1

        # Fill the last row with playable numbers until it's full
        for i in range(startCol, self.colCount):
            try:
                number = next(playableNumbers).copy()
                startRow.set(i, number)

                number.setPosition(Point(self.rowCount - 1, i))
            except StopIteration:
                break

        # Add new rows until we have consumed all playable numbers
        while True:
            newRow = Row.generate(self.colCount, len(self.rows),
                                  [number.copy() for idx, number in enumerate(playableNumbers)
                                   if idx < self.colCount])
            self.rows.append(newRow)

    @staticmethod
    def generate(rowCount: int = None, colCount: int = None, numberRequestAmount: int = None,
                 numbersToGenerate: int = 32, stageNumber: int = 1):
        stage = Stage(0, rowCount, colCount, numberRequestAmount, stageNumber)

        rowsToGenerate = ceil(numbersToGenerate / stage.colCount)
        for i in range(rowsToGenerate):
            remainingCols = stage.colCount if i < rowsToGenerate - 1 else numbersToGenerate % stage.colCount
            newRow = Row.generate(remainingCols, i)
            stage.rows.append(newRow)

        return stage
