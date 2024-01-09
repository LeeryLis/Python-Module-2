from MonopolyGameBoard import MonopolyGameBoard

class Player:
    """ Класс, содержащий параметры игрока """
    last_player_id = 0

    def __init__(self, name: str = None, money: int = 0, position: int = 0, game_board: MonopolyGameBoard = None):
        self.__class__.last_player_id += 1
        self.id = self.__class__.last_player_id

        self.name = name if name is not None else f"Player{self.__class__.last_player_id}"
        self.money = money
        self.position = position
        # Игровая доска должна устанавливаться единожды
        self._game_board = game_board

    @property
    def game_board(self) -> MonopolyGameBoard:
        return self._game_board

    def __str__(self) -> str:
        return f"{self.name} ${self.money}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, money={self.money}, " \
               f"position={self.position}, game_board={self.game_board})"
