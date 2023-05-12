from math import pi, cos, sin

step = 0.2
multiplier = 0.01  # точность числа пи
x = [i*multiplier for i in range(int(-pi/multiplier), int(pi/multiplier), int(step / multiplier))]
y1 = [2*sin(i) for i in x]
y2 = [cos(2*i) for i in x]

print(x, y1, y2, sep='\n')
