# Используя генератор словарей (и не используя код вне него) преобразовать словарь в котором ключами являются
# кортежи из целых чисел в словарь в котором ключом является максимальное значение из чисел исходного ключа, значение
# оставить прежним. Пример: {(2,4):'a', (1,11,1):'b', (2,3):'c'} -> {4:'a', 11:'b', 3:'c'}

dic = {(2, 4): 'a', (1, 11, 1): 'b', (2, 3): 'c'}

dic = {max(k): v for k, v in dic.items()}
print(dic)
