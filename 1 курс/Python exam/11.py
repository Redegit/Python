# Используя генератор списков (и не используя код вне него) преобразовать список содержащий положительные целые
# числа в список, элементами которого являются списки с длиной равной соответствующему числу в первом списке.
# Содержимым вложенных списков являются последовательно идущие целые числа начиная с 1.
# Пример: [3, 1, 4] -> [[1, 2, 3], [1], [1, 2, 3, 4]]

lst = [3, 1, 4]

lst = [[j for j in range(1, i + 1)] for i in lst]
print(lst)
