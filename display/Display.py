import tkinter
from typing import Any


# Abstract class
class Display:
    @staticmethod
    def draw(canvas: tkinter.Canvas, x: int, y: int, entity: Any):
        raise NotImplementedError('draw() not implemented')
