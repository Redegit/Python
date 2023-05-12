from math import factorial, sin, pow

n = 5
x = float(input())
s = 0


def elem(x, n):
    e = pow(-1, n+1) * pow(x, 2*n-1) / factorial(2*n-1)
    return e


for i in range(1, n+1):
    s += elem(x, i)

print(s, sin(x))
