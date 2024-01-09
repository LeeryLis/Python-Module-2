from tiles import Tile
from Player import Player

class BuildingTile(Tile):
    """ Дочерний класс клетки, клетка здания """
    def __init__(self, name: str = None,
                 price: int = 0, level: int = 1, owner: Player = None):
        super().__init__(name)
        self.price = price
        self.level = level
        self.owner = owner

    def __str__(self) -> str:
        if self.owner is not None:
            return f"{self.name} lvl {self.level} ${self.price}; владелец {self.owner.name}"
        return f"{self.name} lvl {self.level} ${self.price}; без владельца"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, " \
               f"price={self.price}, level={self.level}, owner={self.owner})"

    def action_on_occupying(self, player: Player = None):
        """ Имитация игровой логики """
        if self.owner is not None:
            player.money -= self.price
            self.owner.money += self.price
            print(f'{player.name} заплатил игроку {self.owner.name} {self.price}$')
        else:
            if player.money >= self.price:
                player.money -= self.price
                self.owner = player
                print(f"{player.name} теперь владеет предприятием {self.name}")
                self.rename(f"[{self.name} игрока {player.name}]")
