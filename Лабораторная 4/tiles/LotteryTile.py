from tiles import Tile
from Player import Player
import random

class LotteryTile(Tile):
    """ Дочерний класс клетки, клетка лотереи """
    def __init__(self, name: str = "Лотерея", chance: int = 50):
        super().__init__(name)
        self.chance = chance

    @property
    def chance(self) -> int:
        return self._chance

    @chance.setter
    def chance(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Шанс на выигрыш должен быть целым числом процентов")
        if value not in range(0, 101):
            raise ValueError("Шанс на выигрыш должен находиться в границах от 0 до 100 процентов")
        self._chance = value

    def __str__(self) -> str:
        return f"{self.name}; шанс на выигрыш: {self.chance}%"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, chance={self.chance})"

    def action_on_occupying(self, player: Player = None):
        """ Имитация лотереи """
        if random.randint(1, 100) <= self.chance:
            money_win = random.randint(1, 5) * 100
            player.money += money_win
            print(f"{player.name} выиграл {money_win}$")
        else:
            print(f"{player.name} проиграл в лотерее")
