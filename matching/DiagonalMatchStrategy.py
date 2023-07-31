from entities.Point import Point
from matching.MatchStrategy import MatchStrategy


class DiagonalMatchStrategy(MatchStrategy):
    def canMatch(self, source: Point, destiny: Point) -> bool:
        if not super().canMatch(source, destiny):
            return False

        # The difference between the rows and the columns must be the same
        if abs(source.row - destiny.row) != abs(source.col - destiny.col):
            return False

        # Must have a clear path between them
        rowsToCheck = range(min(source.row, destiny.row) + 1, max(source.row, destiny.row))
        colsToCheck = range(min(source.col, destiny.col) + 1, max(source.col, destiny.col))
        for idx in range(len(rowsToCheck)):
            number = self.stage.get(rowsToCheck[idx], colsToCheck[idx])
            if number.isPlayable():
                return False

        return True
