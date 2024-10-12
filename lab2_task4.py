import matplotlib.pyplot as plt
import numpy as np
import random
from math import *

n = 10
N = 10000

def f(phi):
    return sqrt((11 + n) * cos(phi) ** 2 + (11 - n) * sin(phi) ** 2)


X = [f(phi)*cos(phi) for phi in np.arange(0, 2 * pi, 0.00001)]
Y = [f(phi)*sin(phi) for phi in np.arange(0, 2 * pi, 0.00001)]
a = abs(max(X) - min(X))
b = abs(max(Y) - min(Y))

x = [-1]*(N+1)
y = [-1]*(N+1)
r = [-1]*(N+1)
pfi = [-1]*(N+1)

for i in range(1, N + 1):
    x[i] = random.uniform(0, 2*a)
    y[i] = random.uniform(0, 2*b)
    x[i] = x[i] - a
    y[i] = y[i] - b
    r[i] = sqrt(x[i]**2 + y[i]**2)

outside = []
inside = []

for i in range(1, N + 1):
    if (x[i] > 0):
        pfi[i] = atan(y[i]/x[i])
    if (x[i] < 0):
        pfi[i] = pi + atan(y[i]/x[i])
    if (x[i] == 0):
        if (y[i] > 0):
            pfi[i] = pi/2
        elif (y[i] < 0):
            pfi[i] = (-1) * pi/2
        elif (y[i] == 0):
            pfi[i] = 0


for i in range(1, N + 1):
    if (r[i] < f(pfi[i])):
        inside.append((x[i], y[i]))
    else:
        outside.append((x[i], y[i]))


M = len(inside)
S = M/N * a * b * 4

print('Приблизительная площадь S =', round(S, 5))
exact_value = 22*pi/2
print('Точное значение площади:', round(exact_value, 5))
absolute_error = abs(exact_value - S)
print('Абсолютная погрешность:', round(absolute_error, 5))
print('Относительная погрешность:', round(absolute_error / exact_value, 5))

plt.scatter(*zip(*outside), s=5, color='blue')
plt.scatter(*zip(*inside), s=5, color='green')
plt.gca().add_patch(plt.Rectangle(((min(X), max(Y))), a, -b, fill=False, linewidth=2))
plt.plot(X, Y, linewidth=2, color='black')
plt.show()