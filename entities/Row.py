import tkinter
from typing import Union, List

from entities.Number import Number
from entities.Point import Point


class Row:
    def __init__(self, numbers: List[Union[Number, None]] = None, colCount: int = 9):
        self.numbers: List[Union[Number, None]] = [] if numbers is None else numbers
        self.colCount = colCount

    def getPlayableNumbers(self) -> List[Number]:
        numberIsPlayable = lambda n: n.isPlayable()
        return list(filter(numberIsPlayable, self.numbers))

    # TODO optimize so it doesn't have to iterate through the whole list
    def getFirstPlayableNumber(self) -> Number:
        return self.getPlayableNumbers()[0]

    # TODO optimize so it doesn't have to iterate through the whole list
    def getLastPlayableNumber(self) -> Number:
        return self.getPlayableNumbers()[-1]

    def isComplete(self) -> bool:
        return len(self.getPlayableNumbers()) == 0 and len(self.numbers) == self.colCount

    def get(self, index: int) -> Union[Number, None]:
        return self.numbers[index]

    def set(self, index: int, number: Number):
        self.numbers[index] = number

    @staticmethod
    def generate(colCount: int, rowIndex: int, numbersToGenerate: Union[int, None, List[Number]] = None) -> 'Row':
        numbers: List[Number] = []
        if numbersToGenerate is None or isinstance(numbersToGenerate, int):
            numbers = [Number.generate(Point(rowIndex, idx)) for idx in range(numbersToGenerate or colCount)]
        elif isinstance(numbersToGenerate, list):
            numbers = numbersToGenerate

        return Row(numbers, colCount)
