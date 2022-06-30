"""
[*] 1) Объявить класс фигуры (включает конструктор, принимающий координаты фигуры x, y)

[*] 2) Создать объект фигуры

[*] 3) Реализовать для фигуры метод draw (в виде псевдографики на поле 40 на 40 символов), для абстрактной фигуры
рисуем * по заданным координатам

[*] 4) Создать объект фигуры и нарисовать ее

[*] 5) Изменить параметры объекта и перерисовать его

[*] 6) Создать наследника класса фигура – класс прямоугольника, с соответствующим изменением конструктора (рисует в
псевдографике звездочками прямоугольник)

[*] 7) Создать объект прямоугольника и нарисовать его

[*] 8) Изменить параметры объекта и перерисовать его

[*] 9) Создать наследника класса фигура - треугольник (по сложности: 1)прямоуг с одинаковыми катетами 2)просто прямоуг
3)любой треуг)

[*] 10) Создать наслединика класса прямоугольник - класс квадрат

[*] 10) Создать несколько объектов класса треугольник, прямоугольник и фигура, поместить их в список и вызвать функцию
рисования при обходе списка (пример полиморфизма).

[*] *11) Нарисовать ромб(через функцию рисования диагонали)

[*] 12) Создать класс линии (не является наследником фигуры), имеющий метод draw аналогичный предыдущему

[*] 13) Повторить 10 с участием линии (пример утиной типизации)

[*] 14) Реализовать для всех объектов метод, позволяющий печатать объекты при помощи функции print()

[*] 15) Реализовать для фигур функцию расчета площади.

[*] 16) Создать несколько объектов класса треугольник, прямоугольник и фигура, поместить их в список. Расчитать
суммарную площадь всех форм, находящихся в списке.

[*] 17) Для 16 добавить в список объект линия (для которого не реализована функция площади). При помощи функции
определения принадлежности объекта к классу модифицировать рассчет суммарной площади так, чтобы он не приводил к
ошибке.
"""

import math


class Sharp:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.screen = []
        self.allsc = []

    def print_screen(self):
        for line in self.screen:
            pr = ''
            for i in line:
                pr += i
            print(pr)
        print("\n")

    def reload_screen(self):
        self.screen = [['.'] * 40 for _ in range(40)]
        self.allsc = self.screen

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def draw(self):
        self.reload_screen()
        self.screen[self.__y][self.__x] = '*'
        self.print_screen()

    def __str__(self):
        return f'Это точка с координатами ({self.x};{self.y})'

    def area(self):
        return 0

    def raw(self):
        return self.screen


sh = Sharp(x=5, y=6)
sh.draw()

sh.setX(10)
sh.setY(10)

sh.draw()


class Rectangle(Sharp):

    dr = 1
    screen = []

    def scr(self):
        self.screen[self.y][self.x:self.x + self.x] = '*' * self.x
        self.screen[self.y + self.y][self.x:self.x + self.x + 1] = '*' * (self.x + 1)
        for i in range(self.y, self.y + self.y):
            self.screen[i][self.x] = '*'
            self.screen[i][self.x + self.x] = '*'
        self.print_screen()
        return self.screen

    def draw(self):
        if self.dr == 1:
            self.reload_screen()
        if self.y + self.y <= 40 and self.x + self.x <= 40 and self.x != self.y:
            self.scr()
            return self.screen
        else:
            self.exept()

    def exept(self):
        if self.x == self.y:
            print('Прямоугольник не должен иметь равные стороны')
        else:
            print(
                f"В координатах ({self.x};{self.y}) невозможно построить прямоугольник.\nТочка x;y - начало и стороны "
                f"прямоугольника")

    def area(self):
        return self.x * self.y


rc = Rectangle(x=sh.x + 1, y=sh.y)
rc.draw()

rc.setX(7)
rc.setY(4)

rc.draw()


class Square(Rectangle):
    dr = 1
    screen = []

    def draw(self):
        if self.dr == 1:
            self.reload_screen()
        if self.y + self.y <= 40 and self.x + self.x <= 40 and self.x == self.y:
            self.scr()
            return self.screen
        else:
            self.exept()

    def exept(self):
        if self.x != self.y:
            print('Квадрат должен иметь равные стороны')
        else:
            print(
                f"В координатах ({self.x};{self.y}) невозможно построить прямоугольник.\nТочка x;y - начало и стороны "
                f"прямоугольника")

    def area(self):
        return self.x * self.y


sq = Square(x=3, y=3)
sq.draw()


class Triangle(Sharp):
    type = 1
    """
    1)прямоуг с одинаковыми катетами 2)просто прямоуг 3)любой треуг
    """

    dr = 1
    screen = []

    def draw(self):
        if self.dr == 1:
            self.reload_screen()
        if self.type == 1:
            for i in range(self.x, self.x * 2):
                self.screen[(self.y * 2) - 1][i] = '*'
            counter = 0
            self.setX(self.x + (self.x // 2))
            for i in range(self.y, self.y * 2):
                self.screen[i][self.x + counter] = '*'
                self.screen[i][self.x - counter] = '*'
                counter += 1
            self.print_screen()
            return self.screen
        elif self.type == 2:
            for i in range(self.y, self.y + self.y):
                self.screen[i][self.x] = '*'
            self.screen[self.y + self.y][self.x:self.x + self.x] = '*' * self.x
            counter = 0
            for i in range(self.x, self.x + self.x):
                self.screen[self.y + counter][i] = '*'
                counter += 1
            self.print_screen()
            return self.screen
        elif self.type == 3:
            pass
        else:
            print("Тут только 3 типа!")

    def area(self):
        if self.type == 1:
            return (self.x * self.y) / 2
        elif self.type == 2:
            return (math.sqrt(self.x ** 2 + self.y ** 2) * self.y) / 2


tr = Triangle(x=10, y=6)
tr.type = 1
tr.draw()


class Rhombus(Triangle):

    dr = 1
    screen = []

    def draw(self):
        counter = 0
        if self.dr == 1:
            self.reload_screen()
        self.setX(self.x + (self.x // 2))
        for i in range(self.y, self.y * 2):
            self.screen[i][self.x + counter] = '*'
            self.screen[i][self.x - counter] = '*'
            counter += 1
        print(self.y * 4)
        for i in range(self.y * 2, self.y * 4):
            if counter == -1:
                break
            self.screen[i][self.x + counter] = '*'
            self.screen[i][self.x - counter] = '*'
            counter -= 1
        print(self.y * 4)
        self.print_screen()
        return self.screen

    def area(self):
        return (self.x * self.y) / 2


rh = Rhombus(x=10, y=6)
rh.draw()


def prnt(area):
    for line in area:
        pr = ''
        for i in line:
            pr += i
        print(pr)
    print("\n")


prnt(tr.raw() + rc.raw() + sq.raw())


class line:

    dr = 1

    def __init__(self, y, x, type):
        self.__y = y
        self.__x = x
        self.type = type
        self.screen = []

    screen = []

    def reload_screen(self):
        self.screen = [['.'] * 40 for _ in range(40)]

    def draw(self):
        if self.dr == 1:
            self.reload_screen()
        if self.type == 1:
            for i in range(self.__y, self.__y * 2):
                self.screen[i][self.__x] = "*"
        elif self.type == 2:
            self.screen[self.__y][self.__x:self.__x * 2] = "*" * self.__x
        self.print_screen()

    def print_screen(self):
        for line in self.screen:
            pr = ''
            for i in line:
                pr += i
            print(pr)
        print("\n")

    def raw(self):
        return self.screen


# 1 == vertical; 2 == horizontal
ln = line(y=5, x=10, type=2)
ln.draw()

prnt(tr.raw() + rc.raw() + sq.raw() + ln.raw())

sum = 0
for i in [sh, sq, tr]:
    sum += (i.area())

print(sum)

for i in [sh, sq, tr, ln]:
    try:
        sum += (i.area())
    except AttributeError:
        print(f"Нет такой функции для {i.__class__.__name__}")

sh.dr = 0
rc.dr = 0
sq.dr = 0
tr.dr = 0
rh.dr = 0
ln.dr = 0


sq.screen = rc.draw()

tr.screen = sq.draw()

rh.screen = tr.draw()

rh.draw()