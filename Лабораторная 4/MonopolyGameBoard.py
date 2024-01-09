import Player
from collections import deque
import random

class MonopolyGameBoard:
    """ Основной управляющий класс игры """
    def __init__(self, tiles: list, players: deque = None):
        self.players = players if players is not None else deque()
        self.tiles = tiles

    @property
    def tiles(self) -> list:
        return self._tiles

    @tiles.setter
    def tiles(self, tiles_list: list):
        if len(tiles_list) < 1:
            raise ValueError("Поле должно содержать хотя бы одну клетку")
        self._tiles = tiles_list

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(tiles={self.tiles}, players={self.players})"

    def add_player(self, name: str = None, money: int = 0, position: int = 0):
        new_player = Player.Player(name, money, position, self)
        self.players.append(new_player)

    def move(self):
        player = self.players.popleft()
        self.players.append(player)

        dice_number = random.randint(1, 6)  # Бросок кубика
        player.position = (player.position + dice_number) % len(self.tiles)
        print(f"Ходит {player.name}; Число на кубике: {dice_number}")

        self.tiles[player.position].action_on_occupying(player)
