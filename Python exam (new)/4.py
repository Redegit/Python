from math import pi

s = 320

radius = lambda s: (s / pi) ** 0.5
length = lambda s: 2 * pi * (s / pi) ** 0.5

print(length(s), length(123), radius(s), radius(123))
