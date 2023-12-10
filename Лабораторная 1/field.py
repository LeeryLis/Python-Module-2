import doctest
import random

from wizard import Wizard
from power_stone import PowerStone

class Field:
    def __init__(self, size_x: int, size_y: int,
                 wizards_list: list[Wizard] = [], power_stones_list: list[PowerStone] = []):
        """
        Создание и подготовка к работе объекта "Поле"

        :param size_x: размер по x (ширина)
        :param size_y: размер по y (высота)
        :param wizards_list: список Магов
        :param power_stones_list: список Камней

        Примеры:
        >>> field = Field(5, 5)
        >>> field = Field(size_x=15, size_y=10)
        """
        self.size_x = None
        self.size_y = None
        self.init_size(size_x, size_y)

        self.wizards_list = wizards_list
        self.power_stones_list = power_stones_list

    def init_size(self, size_x: int, size_y: int):
        if (size_x <= 0) or (size_y <= 0):
            raise ValueError("Получен некорректный размер поля")
        self.size_x = size_x
        self.size_y = size_y

    def print_field(self):
        # Вывод поля в окно консоли
        array = [["·" for j in range(self.size_y)] for i in range(self.size_x)]

        for wizard in self.wizards_list:
            array[wizard.x][wizard.y] = "W"
        for power_stone in self.power_stones_list:
            array[power_stone.x][power_stone.y] = "s"

        for j in range(self.size_y):
            for i in range(self.size_x):
                print(array[i][j], end='')
            print()

    def is_empty_tile(self, x: int, y: int) -> bool:
        """
        Проверка, есть ли на выбранной клетке Маг или Камень

        :param x: координата x
        :param y: координата y
        :return: является ли клетка пустой

        Примеры:
        >>> field = Field(5, 5)
        >>> field.add_power_stone(PowerStone(field, 0, 2))
        >>> field.is_empty_tile(0, 2)
        False
        >>> field.is_empty_tile(2, 3)
        True
        """

        for wizard in self.wizards_list:
            if (wizard.x == x) and (wizard.y == y):
                return False
        for power_stone in self.power_stones_list:
            if (power_stone.x == x) and (power_stone.y == y):
                return False
        return True

    def get_power_stone_by_position(self, x: int, y: int):
        # Возвращает ссылку на объект Камня, если он был найден по заданной позиции (координаты x, y)
        # В противном случае возвращает None
        for power_stone in self.power_stones_list:
            if (power_stone.x == x) and (power_stone.y == y):
                return power_stone
        return None

    def get_wizards_by_square_position(self, x: int, y: int, distance: int):
        # Возвращает список ссылок на объекты Магов, которые попали в область с центром
        # по координатам x, y и радиусом distance
        wizards = []
        for wizard in self.wizards_list:
            if (abs(wizard.x - x) <= distance) and (abs(wizard.y - y) <= distance):
                wizards.append(wizard)
        return wizards

    def add_wizard(self, wizard: Wizard):
        # Добавление ссылки на объект Мага в список
        self.wizards_list.append(wizard)

    def add_power_stone(self, power_stone: PowerStone):
        # Добавление ссылки на объект Камня в список
        self.power_stones_list.append(power_stone)

    def make_one_move(self):
        # Симуляция одного игрового хода
        # Все Камни получают энергию (+energy_generation)
        # В 50% случаев Камни испускают "аномальное излучение" (50% для каждого камня отдельно)
        for power_stone in self.power_stones_list:
            power_stone.add_energy()
            if random.randint(0, 1) == 1:
                power_stone.abnormal_radiation()


if __name__ == "__main__":
    doctest.testmod()
