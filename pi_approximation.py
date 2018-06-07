import random
from math import sqrt

CANTIDAD_DE_PUNTOS = 10000000


def aproximar_pi():
    puntos_dentro_circulo = 0

    for i in range(CANTIDAD_DE_PUNTOS):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if sqrt(x**2 + y**2) <= 1:
            puntos_dentro_circulo += 1

    return (puntos_dentro_circulo / CANTIDAD_DE_PUNTOS) * 4.0


print(aproximar_pi())
