# Вычислите площадь треугольника по двум сторонам и углу между ними

import math

a = float(input('Введите длину стороны А: '))
b = float(input('Введите длину стороны В: '))
# с = int(input('Введите значение угла: '))
s = 1 / 2 * a * b * math.sin(65)
print(f'Площадь треугольника равна: {s}')
