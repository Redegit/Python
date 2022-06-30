from math import factorial, cos, pow

s = 0
x = float(input())
n = 5


def elem(x, n):
    e = pow(-1, n) * pow(x, 2*n) / factorial(2*n)
    return e


for i in range(n):
    s += elem(x, i)

print(s, cos(x))

# при n = 5 программа корректно считает примерно до x = 3 радиана, при х = 4 уже сходит с ума; увеличить n при большем x
