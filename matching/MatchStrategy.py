from entities.Point import Point
from entities.Stage import Stage


class MatchStrategy:
    def __init__(self, stage: Stage):
        self.stage = stage

    def canMatch(self, source: Point, destiny: Point) -> bool:
        sourceNumber = self.stage.get(source.row, source.col)
        destinyNumber = self.stage.get(destiny.row, destiny.col)

        if sourceNumber is None or destinyNumber is None:
            return False

        if not sourceNumber.canMatch(destinyNumber):
            return False

        return True
