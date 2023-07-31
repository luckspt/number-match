from random import randint
from typing import Self

from entities.Point import Point


class Number:
    def __init__(self, number: int, position: Point, used: bool = False, selected: bool = False):
        self.value = number
        self.used = used
        self.selected = selected
        self.position = position

    def setPosition(self, position: Point):
        self.position = position

    def use(self):
        self.used = True
        self.selected = False

    def isPlayable(self) -> bool:
        return not self.used

    def canMatch(self, other: Self) -> bool:
        return self.value is not None and self.value == other.value or self.value + other.value == 10

    def copy(self):
        return Number(self.value, self.position, self.used, self.selected)

    @staticmethod
    def generate(position: Point) -> 'Number':
        return Number(randint(1, 1), position)
