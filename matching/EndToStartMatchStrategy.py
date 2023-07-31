from entities.Point import Point
from matching.MatchStrategy import MatchStrategy


class EndToStartMatchStrategy(MatchStrategy):
    def canMatch(self, source: Point, destiny: Point) -> bool:
        if not super().canMatch(source, destiny):
            return False

        # Must be in the row exactly above
        if source.row + 1 != destiny.row:
            return False

        # Must be the last playable number of the source
        # and the first playable number of the destiny
        # We compare the objects because we want to know if they are the same instance
        lastPlayableNumber = self.stage.rows[source.row].getLastPlayableNumber()
        if lastPlayableNumber.position != source:
            return False

        firstPlayableNumber = self.stage.rows[destiny.row].getFirstPlayableNumber()
        if firstPlayableNumber.position != destiny:
            return False

        return True
