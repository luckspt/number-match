import tkinter
from math import floor
from typing import Union

from display.Display import Display
from display.Number import NUMBER_SQUARE_WIDTH, DisplayNumber
from entities.Number import Number
from entities.Row import Row


class DisplayRow(Display):
    @staticmethod
    def getSelectedNumber(x: int, entity: Row) -> Union[Number, None]:
        numberIndex = floor(x / NUMBER_SQUARE_WIDTH)
        if numberIndex < 0 or numberIndex >= len(entity.numbers):
            return None

        return entity.numbers[numberIndex]

    @staticmethod
    def draw(canvas: tkinter.Canvas, x: int, y: int, entity: Row):
        for idx, number in enumerate(entity.numbers):
            if number is not None:
                DisplayNumber.draw(canvas, x + (idx * NUMBER_SQUARE_WIDTH), y, number)
