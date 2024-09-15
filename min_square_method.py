import matplotlib.pyplot as plt
import math

x = [2, 4, 6, 8, 10, 12]
y = [2.4, 2.9, 3.0, 3.5, 3.6, 3.7]
# y = ax + b
# y = beta * x ** a
# y = beta * e ** (ax)
# y = ax**2 + bx + c

plt.scatter(x, y, color='black')
plt.xlabel('Ось х')
plt.ylabel('Ось y')

def round_with_precision(value, eps = 0.0001):
    return round(value / eps) * eps

def det_3x3(a, b, c, d, e, f, g, h, i):
    # Метод треугольника для нахождения определителя 3x3 матрицы
    return a * e * i + b * f * g + c * d * h - (c * e * g + b * d * i + a * f * h)

def linear_min_square_method(x, y):
    n = len(x)
    summa_square_x = 0
    summa_x = 0
    summa_y = 0
    summa_x_y = 0
    for i in range (len(x)):
        summa_square_x += x[i] ** 2
        summa_x += x[i]
        summa_y += y[i]
        summa_x_y += x[i] * y[i]
    main_det = round_with_precision(summa_square_x * n - summa_x * summa_x)
    a = round_with_precision((summa_x_y * n - summa_y * summa_x) / main_det)
    b = round_with_precision((summa_square_x * summa_y - summa_x * summa_x_y) / main_det)

    a = round(a, 2)
    b = round(b, 2)

    return a, b

def power_min_square_method(x, y):
    n = len(x)
    summa_ln_square_x = 0
    summa_ln_x = 0
    summa_ln_y = 0
    summa_ln_x_y = 0
    for i in range (len(x)):
        summa_ln_square_x += math.log(x[i]) ** 2
        summa_ln_x += math.log(x[i])
        summa_ln_y += math.log(y[i])
        summa_ln_x_y += math.log(x[i]) * math.log(y[i])
    main_det = round_with_precision(summa_ln_square_x * n - summa_ln_x ** 2)
    a = round_with_precision((summa_ln_x_y * n - summa_ln_y * summa_ln_x) / main_det)
    b = round_with_precision((summa_ln_square_x * summa_ln_y - summa_ln_x * summa_ln_x_y) / main_det)
    
    a = round(a, 2)
    beta = round(math.exp(b), 2)
    return a, beta

def exp_min_square_method(x, y):
    n = len(x)
    summa_square_x = 0
    summa_x = 0
    summa_ln_y = 0
    summa_x_ln_y = 0
    for i in range (len(x)):
        summa_square_x += x[i] ** 2
        summa_x += x[i]
        summa_ln_y += math.log(y[i])
        summa_x_ln_y += x[i] * math.log(y[i])
    main_det = round_with_precision(summa_square_x * n - summa_x ** 2)
    a = round_with_precision((summa_x_ln_y * n - summa_ln_y * summa_x) / main_det)
    b = round_with_precision((summa_square_x * summa_ln_y - summa_x * summa_x_ln_y) / main_det)
    
    a = round(a, 2)
    beta = round(math.exp(b), 2)
    return a, beta

def sq_min_square_method(x, y):
    n = len(x)
    summa_4_x = 0
    summa_3_x = 0
    summa_2_x = 0
    summa_x = 0
    summa_y = 0
    summa_x_y = 0
    summa_2_x_y = 0
    for i in range (len(x)):
        summa_4_x += x[i] ** 4
        summa_3_x += x[i] ** 3
        summa_2_x += x[i] ** 2
        summa_x += x[i]
        summa_y += y[i]
        summa_x_y += x[i] * y[i]
        summa_2_x_y += (x[i] ** 2) * y[i]
    main_det = det_3x3(summa_4_x, summa_3_x, summa_2_x, summa_3_x, summa_2_x, summa_x, summa_2_x, summa_x, n)
    det_1 = det_3x3(summa_2_x_y, summa_3_x, summa_2_x, summa_x_y, summa_2_x, summa_x, summa_y, summa_x, n)
    det_2 = det_3x3(summa_4_x, summa_2_x_y, summa_2_x, summa_3_x, summa_x_y, summa_x, summa_2_x, summa_y, n)
    det_3 = det_3x3(summa_4_x, summa_3_x, summa_2_x_y, summa_3_x, summa_2_x, summa_x_y, summa_2_x, summa_x, summa_y)
    a = round_with_precision(det_1 / main_det)
    b = round_with_precision(det_2 / main_det)
    c = round_with_precision(det_3 / main_det)
    
    a = round(a, 2)
    b = round(b, 2)
    c = round(c, 2)
    return a, b, c

def check_lin(a, b, x, y):
    summa = 0
    for i in range(len(x)):
        summa += (y[i] - (a * x[i] + b)) ** 2
    return summa

def check_pow(a, beta, x, y):
    summa = 0
    for i in range(len(x)):
        summa += (y[i] - (beta * (x[i] ** a))) ** 2
    return summa

def check_exp(a, beta, x, y):
    summa = 0 
    for i in range(len(x)):
        summa += (y[i] - (beta * math.exp(a * x[i]))) ** 2
    return summa

def check_sq(a, b, c, x, y):
    summa = 0
    for i in range(len(x)):
        summa += (y[i] - (a * (x[i]) ** 2 + b * x[i] + c)) ** 2
    return summa

a_lin,b_lin = linear_min_square_method(x, y)
y_new_lin = [(a_lin * x[i] + b_lin) for i in range(len(x))]
plt.plot(x, y_new_lin, color='green', label='Линейная аппроксимация')

a_pow,beta_pow = power_min_square_method(x, y)
y_new_pow = [beta_pow * (x[i] ** a_pow) for i in range(len(x))]
plt.plot(x, y_new_pow, color='blue', label='Степенная аппроксимация')

a_exp,beta_exp = exp_min_square_method(x, y)
y_new_exp = [beta_exp * math.exp(x[i] * a_exp) for i in range(len(x))]
plt.plot(x, y_new_exp, color='red', label='Показательная аппроксимация')

a_sq, b_sq, c_sq = sq_min_square_method(x, y)
y_new_sq = [(a_sq * x[i] ** 2 + b_sq * x[i] + c_sq) for i in range(len(x))]
plt.plot(x, y_new_sq, color='violet', label='Квадратичная аппроксимация')

plt.legend()
plt.show()

minimal_exp = min(check_lin(a_lin, b_lin, x, y), check_pow(a_pow, beta_pow, x, y), check_exp(a_exp, beta_exp, x, y), check_sq(a_sq, b_sq, c_sq, x, y))
print("Погрешность линейной аппроксимации: ", check_lin(a_lin, b_lin, x, y))
print("Погрешность степенной аппроксимации: ", check_pow(a_pow, beta_pow, x, y))
print("Погрешность показательной аппроксимации: ", check_exp(a_exp, beta_exp, x, y))
print("Погрешность квадратичной аппроксимации: ", check_sq(a_sq, b_sq, c_sq, x, y))
print("Минимальная погрешность: ", minimal_exp)