from Player import Player

class Tile:
    """ Родительский класс всех клеток, основная пустая клетка """
    def __init__(self, name: str = "Nothing"):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"

    def rename(self, new_name: str):
        self.name = new_name

    def action_on_occupying(self, player: Player = None):
        print(f"{player.name} встал на клетку {self.name}")
