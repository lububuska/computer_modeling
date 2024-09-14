import matplotlib.pyplot as plt

eps = 0.0001
x = [2, 4, 6, 8, 10, 12]
y = [2.4, 2.9, 3.0, 3.5, 3.6, 3.7]



plt.scatter(x, y)
plt.show()
def min_square_method(x, y):
    n = len(x)
    summa_square_x = 0
    summa_x = 0
    summa_y = 0
    summa_x_y = 0
    for i in range (len(x)):
        summa_square_x += x[i] ** 2
        summa_x += x[i]
    for i in range(len(y)):
        summa_y += y[i]
        summa_x_y += x[i] * y[i]
    main_det = summa_square_x * n - summa_x * summa_x
    a = (summa_x_y * n - summa_y * summa_x) / main_det
    b = (summa_square_x * summa_y - summa_x * summa_x_y) / main_det
    return a, b

new_y = a * x + b

print(min_square_method(x, y))