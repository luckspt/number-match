from math import ceil
from typing import Union, List
from entities.Row import Row


class Stage:
    def __init__(self, goal: int, rowCount: int = 13, colCount: int = 9, numberRequestAmount: int = 5):
        self.goal = goal
        self.rowCount = rowCount
        self.colCount = colCount
        self.rows: List[Union[Row, None]] = []
        self.numberRequestAmount = numberRequestAmount

    def get(self, row: int, col: int):
        return self.rows[row].get(col)

    def requestMoreNumbers(self):
        pass

    @staticmethod
    def generate(self, numbersToGenerate: int = 32):
        rowsToGenerate = ceil(numbersToGenerate / self.colCount)
        for i in range(rowsToGenerate):
            remainingCols = self.colCount if i < rowsToGenerate - 1 else numbersToGenerate % self.colCount
            newRow = Row.generate(remainingCols)
            self.rows.append(newRow)
