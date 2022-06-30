from math import sqrt, pow


def def_quarter(x, y):
    if x * y < 0:
        if x < 0:
            return "2nd quarter", 2
        else:
            return "4th quarter", 4
    elif x * y > 0:
        if x > 0:
            return "1st quarter", 1
        else:
            return "3rd quarter", 3
    else:
        if x == 0 and y == 0:
            return "The point at the origin", 0
        elif x == 0:
            return "The point is on y-axis", 0
        else:
            return "The point is on x-axis", 0


x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

location = def_quarter(x, y)
print(location[0])
print(location[1] * sqrt(pow(x, 2) + pow(y, 2)))
