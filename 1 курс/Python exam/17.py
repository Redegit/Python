# Реализовать функцию nam_par, которая принимает на вход заранее неизвестное количество параметров и необязательный
# параметр name в который можно передать строку. Функция возвращает словарь в котором переданные параметры являются
# значениями, ключами для них являются соответсвующие (сопоставленные по порядку следования) символы из строки name.
# Если строка name не задана, то значения присваиваются по порядку английского алфавита.
# Пример 1: nam_par(7, 3, 1, 8, 10, 13, name='xyzafg') -> {'x':7, 'y':3, 'z':1, 'a':8, 'f':10, 'g':13}
# Пример 2: nam_par(21, 'val', -3.5) -> {'a':21, 'b':'val', 'c':-3.5}

import string


# string.ascii_letters - строка со всеми буквами английского алфавита
# (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
def nam_par(*p, name=string.ascii_letters):
    dic = {letter: par for letter, par in zip(name, p)}
    return dic


print(nam_par(7, 3, 1, 8, 10, 13, name='xyzafg'))
print(nam_par(21, 'val', -3.5))
