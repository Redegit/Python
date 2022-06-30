from tabulate import tabulate
from random import randint


n = 4
matrix = [[randint(-100, 100) for i in range(n)] for i in range(n)]
print(tabulate(matrix, tablefmt="fancy_grid", stralign='center'))

main_summ = secondary_summ = main_count = secondary_count = 0

for i, j in zip(range(n), range(n)):
    if matrix[i][j] > 0:
        main_summ += matrix[i][j]
        main_count += 1

for i, j in zip(range(n-1, -1, -1), range(n)):
    if matrix[i][j] < 0:
        secondary_summ += matrix[i][j]
        secondary_count += 1

try:
    print(f"Среднее арифметическое положительных элементов главной диагонали: {main_summ / main_count}")
except ZeroDivisionError:
    print("На главной диагонали нет положительных элементов")

try:
    print(f"Среднее арифметическое отрицательных элементов побочной диагонали: {secondary_summ / secondary_count}")
except ZeroDivisionError:
    print("На побочной диагонали нет отрицательных элементов")
