import tkinter

from display.Display import Display
from entities.Number import Number

NUMBER_SQUARE_WIDTH = 30
NUMBER_SQUARE_HEIGHT = 30
NUMBER_SQUARE_OUTLINE_THICKNESS = 2
NUMBER_SQUARE_OUTLINE_COLOR = 'gray'
NUMBER_TEXT_SIZE = 20


class DisplayNumber(Display):
    @staticmethod
    def draw(canvas: tkinter.Canvas, x: int, y: int, entity: Number):
        canvas.create_rectangle(x, y, x + NUMBER_SQUARE_WIDTH, y + NUMBER_SQUARE_HEIGHT,
                                fill='white' if not entity.selected else 'light cyan')
        canvas.create_text(x + NUMBER_SQUARE_WIDTH / 2, y + NUMBER_SQUARE_HEIGHT / 2, text=entity.value,
                           font=('Arial', NUMBER_TEXT_SIZE), fill='black' if not entity.used else 'light gray')
