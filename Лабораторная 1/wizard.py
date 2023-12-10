class Wizard:
    def __init__(self, field, x: int, y: int, name: str = "Unknown Wizard",
                 intelligence: int = 10, max_energy: int = 100, current_energy: int = 0):
        self.field = field

        self.x = None
        self.y = None
        self._init_position(x, y)

        self.name = name

        self.intelligence = self._is_valid_intelligence(intelligence)

        self.max_energy = self._is_valid_max_energy(max_energy)
        self.current_energy = self._is_valid_current_energy(current_energy)

    def __str__(self):
        # Переопределение медода __str__ для удобного вывода характеристик объекта
        return f"{self.name}; I = {self.intelligence}; [x:{self.x}, y:{self.y}]; {self.current_energy}/{self.max_energy}"

    def _init_position(self, x: int, y: int):
        if not self.field.is_empty_tile(x, y):
            raise ValueError("Данная клетка занята")
        self.x = x
        self.y = y

    def _is_valid_intelligence(self, intelligence: int):
        if intelligence <= 0:
            raise ValueError("Интеллект должен быть положительным числом")
        return intelligence

    def _is_valid_max_energy(self, max_energy: int):
        if max_energy <= 0:
            raise ValueError("Максимальная энергия должна быть положительным числом")
        return max_energy

    def _is_valid_current_energy(self, current_energy: int):
        if (current_energy < 0):
            raise ValueError("Текущая энергия должна быть неотрицательным числом")
        if (current_energy > self.max_energy):
            raise ValueError("Текущая энергия должна быть не больше максимальной энергии")
        return current_energy

    def add_intelligence(self, amount: int):
        # Изменение интеллекта на +amount
        self.intelligence += amount

    def absorb_energy(self, x: int, y: int):
        # "Впитывание" Магом энергии из соседнего Камня (энергия Камня уменьшается, энергия Мага увеличивается)
        # Производится проверка наличия камня по заданным координатам x, y,
        # а также "соседство" Мага с выбранными координатами
        if (abs(self.x - x) <= 1) and (abs(self.y - y) <= 1):
            power_stone = self.field.get_power_stone_by_position(x, y)
            if power_stone is not None:
                difference = self.max_energy - self.current_energy
                stone_energy = power_stone.current_energy
                if difference >= stone_energy:
                    self.current_energy += stone_energy
                    power_stone.reduce_energy(stone_energy)
                else:
                    self.current_energy = self.max_energy
                    power_stone.reduce_energy(difference)
            else:
                raise ValueError("Камень Энергии не найден")
        else:
            raise ValueError("Выбрана не соседняя клетка")
