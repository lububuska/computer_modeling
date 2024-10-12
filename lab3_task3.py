def lemer(R0, g, N):
    random_numbers = []
    random_numbers.append(R0)
    for _ in range(1, N):
        next_value = round(((g * R0) % 1), 4)
        random_numbers.append(next_value)
        R0 = next_value
    return random_numbers

R0 = 0.585  
g = 927  
N = 5  
print(lemer(R0, g, N))
