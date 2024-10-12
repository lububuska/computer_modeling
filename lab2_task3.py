import matplotlib.pyplot as plt
import random
from math import pi

R = 10
N = 10000


z = [-1]*(2*N + 1)

for i in range (1, 2*N + 1):
    z[i] = random.uniform(0, 2*R) #массив случайных координат

x = [i for i in z]
y = [-1]*(N + 1)
for j in range (1, N+1):
    y[j] = z[j+N]

outside = []
inside = []

for i in range (1, N + 1):
    if ((x[i] - R)**2 + (y[i] - R)**2 < R**2):
        inside.append((x[i], y[i]))
    else:
        outside.append((x[i], y[i]))

M = len(inside)
p_i = M/N * 4

print('Вычисленное значение пи =', p_i)
print('Значение числа пи из бибиотеки math:', pi)
absolute_error = abs(pi-p_i)
print('Абсолютная погрешность:', round(absolute_error, 5))
print('Относительная погрешность:', round(absolute_error / pi, 5))

plt.scatter(*zip(*outside), s=7, color = 'blue', label="Точки снаружи")
plt.scatter(*zip(*inside), s=7, color = 'green', label="Точки внутри")
plt.gca().add_patch(plt.Rectangle((0, 0), 2 * R, 2 * R, fill=False, linewidth=2))
plt.gca().add_patch(plt.Circle((R, R), R, fill=False, linewidth=2, color = 'black'))
plt.axis('equal')
plt.show()