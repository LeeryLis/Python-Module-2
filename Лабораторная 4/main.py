from tiles import Tile, BuildingTile, ChanceTile, LotteryTile
from MonopolyGameBoard import MonopolyGameBoard

import random

def print_players(game_board: MonopolyGameBoard):
    """ Вывести в консоль всех игроков """
    print("-"*50)
    print("Игроки:")
    print("-"*50)
    for player in game_board.players:
        print(player)
    print("-"*50)

def print_tiles(game_board: MonopolyGameBoard):
    """ Вывести в консоль все игровые клетки """
    print("-" * 50)
    print("Игровое поле:")
    print("-" * 50)
    for tile in game_board.tiles:
        print(tile)
    print("-" * 50)

def create_game_tiles(empty_count: int = 0, chance_count: int = 0,
                              lottery_count: int = 0, building_count: int = 0) -> list:
    tiles_list = [Tile() for i in range(empty_count)]
    tiles_list.extend([ChanceTile() for i in range(chance_count)])
    tiles_list.extend([LotteryTile(chance=random.randint(1, 10) * 10) for i in range(lottery_count)])
    tiles_list.extend([BuildingTile(f"Здание {i+1}", random.randint(1, 5) * 100) for i in range(building_count)])

    random.shuffle(tiles_list)

    tiles_list.insert(0, Tile("Старт"))

    return tiles_list


if __name__ == "__main__":
    # Создание клеток
    game_tiles = create_game_tiles(2, 2, 4, 4)

    monopoly_game_board = MonopolyGameBoard(game_tiles)

    # Добавление игроков
    for _ in range(3):
        monopoly_game_board.add_player(money=10_000)

    print_players(monopoly_game_board)
    print_tiles(monopoly_game_board)

    # Имитация игры
    for i in range(0, len(monopoly_game_board.players) * 3):
        monopoly_game_board.move()
        print()

    print_players(monopoly_game_board)
    print_tiles(monopoly_game_board)

    # Тест вывода __repr__
    print()
    print(repr(monopoly_game_board))
    print(repr(monopoly_game_board.players[0]))
    print(repr(Tile()))
    print(repr(ChanceTile()))
    print(repr(LotteryTile(chance=random.randint(1, 10) * 10)))
    print(repr(BuildingTile(f"Здание {1}", random.randint(1, 5) * 100)))
