from time import sleep

class TrafLight:
    __color = "Чёрный"

    def running(self):
        while True:
            print("TrafLight is red now")
            sleep(2)
            print("TrafLight is yellow now")
            sleep(2)
            print("TrafLight is green now")
            sleep(2)
            print("TrafLight is yellow now")
            sleep(1)

traflight=TrafLight()
traflight.running()

"""class Road:
    mass_1 = 25
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self):
        thickness = int(input('Какой толщины положить асфальт? '))
        print(f'Необходимо {self._lenght * self._width * self.mass_1 * thickness / 1000} тонн асфальта')


lenin_street = Road(1000, 10)
lenin_street.mass()

class Road:
    def __init__(self, lenght, width):
        self._lenght=lenght
        self._width=width
    def profit(self, weight=25, thickness=5):
        return f'{self._lenght} m * {self._width} m * {weight} кг *{thickness} см ='\
               f"{(self._lenght * self._width * weight * thickness)/1000} т"
road_1=Road(5000, 20)
print(road_1.profit())

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name=name
        self.surname=surname
        self.position=position
        self._income={'profit': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_ful_profit(self):
        return f'{sum(self._income.values())}'

manager = Position('Jack', 'Daniels', 'Chief', 60000, 800000)

print(manager.get_full_name())
print(manager.position)
print(manager.get_ful_profit())
"""
