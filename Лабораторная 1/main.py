from field import Field
from wizard import Wizard
from power_stone import PowerStone

field = Field(5, 5)

field.add_wizard(Wizard(field, x=1, y=2, name="Dumbledore", current_energy=70, max_energy=80))
field.add_wizard(Wizard(field, 2, 4))

field.add_power_stone(PowerStone(field, x=1, y=1, current_energy=24, energy_generation=3))
field.add_power_stone(PowerStone(field, 4, 2, 10, 5))

field.print_field()

for power_stone in field.power_stones_list:
    print(power_stone)

field.make_one_move()
print()

for power_stone in field.power_stones_list:
    print(power_stone)

print()
print(field.wizards_list[0])
print(field.power_stones_list[0])
field.wizards_list[0].absorb_energy(1, 1)
print(field.wizards_list[0])
print(field.power_stones_list[0])
