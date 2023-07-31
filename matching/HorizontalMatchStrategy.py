from entities.Point import Point
from matching.MatchStrategy import MatchStrategy


class HorizontalMatchStrategy(MatchStrategy):
    def canMatch(self, source: Point, destiny: Point) -> bool:
        if not super().canMatch(source, destiny):
            return False

        # Must be on the same row, and the column be another
        if source.row != destiny.row or source.col == destiny.col:
            return False

        # Must have a clear path between them
        rowNumbers = self.stage.rows[source.row].numbers[min(source.col, destiny.col)+1:max(source.col, destiny.col)]
        for number in rowNumbers:
            if number.isPlayable():
                return False

        return True
