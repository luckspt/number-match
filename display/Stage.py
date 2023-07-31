import tkinter
from math import floor
from typing import Union

from display.Display import Display
from display.Number import NUMBER_SQUARE_WIDTH, NUMBER_SQUARE_HEIGHT
from display.Row import DisplayRow
from entities.Row import Row
from entities.Stage import Stage

STAGE_OUTLINE_THICKNESS = 5
STAGE_OUTLINE_COLOR = 'black'


class DisplayStage(Display):
    @staticmethod
    def getSelectedRow(y: int, entity: Stage) -> Union[Row, None]:
        rowIndex = floor(y / NUMBER_SQUARE_HEIGHT)
        if rowIndex < 0 or rowIndex >= len(entity.rows):
            return None

        return entity.rows[rowIndex]

    @staticmethod
    def draw(canvas: tkinter.Canvas, x: int, y: int, entity: Stage):
        for idx, row in enumerate(entity.rows):
            DisplayRow.draw(canvas, x, y + idx * NUMBER_SQUARE_HEIGHT, row)

        # Draw greater outline
        canvas.create_rectangle(x, y,
                                (entity.colCount * NUMBER_SQUARE_WIDTH) + STAGE_OUTLINE_THICKNESS * 2,
                                (entity.rowCount * NUMBER_SQUARE_HEIGHT) + STAGE_OUTLINE_THICKNESS * 2,
                                outline=STAGE_OUTLINE_COLOR, width=STAGE_OUTLINE_THICKNESS)
