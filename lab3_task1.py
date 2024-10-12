def Neiman(R0, N):
    random_numbers = []
    random_numbers.append(R0)
    for _ in range(N-1):
        square_str = str(R0).replace('0.', '')  # Убираем точку и 0 из строки
        square = str(int(square_str) ** 2)        
        mid_index = len(square) // 2
        # Извлекаем 4 цифры из середины
        R0 = "0." + square[mid_index - 2 : mid_index + 2]
        random_numbers.append(float(R0))  # Преобразуем обратно в float для удобства
    return random_numbers

R0 = 0.583
N = 6

print(Neiman(R0, N))