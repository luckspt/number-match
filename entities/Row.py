from typing import Union, List

from entities.Number import Number


class Row:
    def __init__(self, numbers: List[Union[Number, None]] = None, colCount: int = 9):
        self.numbers: List[Union[Number, None]] = [] if numbers is None else numbers
        self.colCount = colCount

    def getPlayableNumbers(self) -> List[Number]:
        numberIsPlayable = lambda n: n.isPlayable()
        return list(filter(numberIsPlayable, self.numbers))

    def getFirstPlayableNumber(self) -> Number:
        return self.getPlayableNumbers()[0]

    def getLastPlayableNumber(self) -> Number:
        return self.getPlayableNumbers()[-1]

    def isComplete(self) -> bool:
        return len(self.getPlayableNumbers()) == 0 and len(self.numbers) == self.colCount

    def get(self, index: int) -> Union[Number, None]:
        return self.numbers[index]

    def set(self, index: int, number: Number):
        self.numbers[index] = number

    @staticmethod
    def generate(colCount: int, numbersToGenerate: int = None) -> 'Row':
        if numbersToGenerate is None:
            numbersToGenerate = colCount

        return Row([Number.generate() for _ in range(numbersToGenerate)], colCount)
