class PowerStone:
    def __init__(self, field, x: int, y: int, current_energy: int = 0, energy_generation: int = 1):
        self.field = field

        self.x = None
        self.y = None
        self._init_position(x, y)

        self.current_energy = self._is_valid_current_energy(current_energy)
        self.energy_generation = self._is_valid_energy_generation(energy_generation)

    def __str__(self):
        return f"Power Stone [x:{self.x}, y:{self.y}]; {self.current_energy}; +{self.energy_generation}"

    def _init_position(self, x: int, y: int):
        if not self.field.is_empty_tile(x, y):
            raise ValueError("Данная клетка занята")
        self.x = x
        self.y = y

    def _is_valid_current_energy(self, current_energy: int):
        if current_energy < 0:
            raise ValueError("Запас энергии должен быть неотрицательным числом")
        return current_energy

    def _is_valid_energy_generation(self, energy_generation: int):
        if energy_generation <= 0:
            raise ValueError("Генерация энергии должна быть положительным числом")
        return energy_generation

    def add_energy(self):
        # Добавление energy_generation к текущей энергии Камня
        self.current_energy += self.energy_generation

    def reduce_energy(self, amount: int):
        # Уменьшение энергии Камня на заданное значение
        self.current_energy -= amount

    def abnormal_radiation(self):
        # Симуляция "аномального излучения"
        # Производится поиск всех соседних магов (метод в классе Field)
        # Затем у выбранных магов интеллект возрастает на 2 пункта
        wizards = self.field.get_wizards_by_square_position(self.x, self.y, 1)

        for wizard in wizards:
            wizard.add_intelligence(2)
