from math import *
import matplotlib.pyplot as plt
import numpy as np
import random

n = 10
N = 10000

def f(x):
    return sqrt(11 - n * sin(x)*sin(x))

a = 5
b = 3.4

x=[-1]*(N+1)
y=[-1]*(N+1)
outside = []
inside = []

for i in range (1, N+1):
    x[i] = random.uniform(0,a)
    y[i] = random.uniform(0,b)
    if (y[i] < f(x[i])):
        inside.append((x[i],y[i]))
    else:
        outside.append((x[i],y[i]))

M = len(inside)
S = M/N*a*b

print('Приблизительная площадь S =', round(S, 5))
exact_value = 11.240289750440605
print('Точное значение площади:', round(exact_value, 5))
absolute_error = abs(exact_value-S)
print('Абсолютная погрешность:', round(absolute_error, 5))
print('Относительная погрешность:', round(absolute_error / exact_value, 5))

if inside:
    plt.scatter(*zip(*inside), s=5, color='green', label="Точки внутри")
if outside:
    plt.scatter(*zip(*outside), s=5, color='blue', label="Точки вне")
X = np.arange(0.01, a, 0.00001)
plt.plot(X, [f(x) for x in X], linewidth=2, color='black')
plt.show()