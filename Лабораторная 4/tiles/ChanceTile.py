from tiles import Tile
from Player import Player

class ChanceTile(Tile):
    """ Дочерний класс клетки, клетка шанса """
    def __init__(self, name: str = "Шанс"):
        super().__init__(name)

    def action_on_occupying(self, player: Player = None):
        """ Можно реализовать логику карт """
        print(f'{player.name} тянет карту "шанс"')
