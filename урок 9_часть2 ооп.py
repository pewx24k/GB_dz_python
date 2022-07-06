
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула {direction.lower()}')
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        msg = (f'Текущая скорость {self.speed} км/ч'
               if self.speed <= 60 else f'Скорость {self.speed} км/ч выше разрешённой')
        print(msg)

class SportCar(Car):
    def show_police(self):
        if self.is_police:
            print('Это полицейская машина')

class WorkCar(Car):
    def show_speed(self):
        msg = (f'Текущая скорость {self.speed} км/ч'
               if self.speed <= 40 else f'Скорость {self.speed} км/ч выше разрешённой')
        print(msg)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if not self.is_police:
            print('Это не полицейская машина')

a = TownCar(70, 'yellow', 'легковушка', False)
a.show_speed()
b = WorkCar(40, 'grey', 'мусоровоз', False)
b.turn('Влево')
print(b.name)
p = PoliceCar(100, 'white-blue', 'Cop', False)
print(p.color)
s = SportCar(150, 'Red', 'Hooligan', True)

s.show_police()


class Stationery:
    def __init__(self, title):
        self.title = title

class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')

class Pencil(Stationery):
    def draw(self):
        print('Карандаш может писать вверх ногами')

class Handle(Stationery):
    def draw(self):
        print('С помощью него можно выделить текст')

pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

pen.draw()
pencil.draw()
handle.draw()