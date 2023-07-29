from random import randint
from typing import Self


class Number:
    def __init__(self, number: int, used: bool = False):
        self.value = number
        self.used = used

    def isPlayable(self) -> bool:
        return not self.used

    def canMatch(self, other: Self) -> bool:
        return self.value is not None and self.value == other.value or self.value + other.value == 10

    @staticmethod
    def generate() -> 'Number':
        return Number(randint(1, 9))
