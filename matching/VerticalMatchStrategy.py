from entities.Point import Point
from matching.MatchStrategy import MatchStrategy


class VerticalMatchStrategy(MatchStrategy):
    def canMatch(self, source: Point, destiny: Point) -> bool:
        if not super().canMatch(source, destiny):
            return False

        # Must be in a different row, and the column be the same
        if source.row == destiny.row or source.col != destiny.col:
            return False

        # Must have a clear path between them
        rowsToCheck = range(min(source.row, destiny.row) + 1, max(source.row, destiny.row))
        for row in rowsToCheck:
            number = self.stage.get(row, source.col)
            if number.isPlayable():
                return False

        return True
