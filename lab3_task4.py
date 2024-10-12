def multiplicative_congruential_method(X0, a, m, N):
    random_numbers_X = []
    random_numbers_X.append(X0)
    for _ in range(1, N):
        next_value = (a * X0) % m
        random_numbers_X.append(next_value)
        X0 = next_value
    R = []
    for i in range(len(random_numbers_X)):
        R_i = random_numbers_X[i] / m
        R.append(R_i)
    return R

X0 = 122  
a = 265  
m = 129  
N = 5  

print(multiplicative_congruential_method(X0, a, m, N))
