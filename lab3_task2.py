def Neiman(R0, R1, N):
    random_numbers = []
    random_numbers.append(R0)
    random_numbers.append(R1)
    for _ in range(N-2):
        square_str0 = str(R0).replace('0.', '')  
        square_str1 = str(R1).replace('0.', '')  
        square0 = int(square_str0)        
        square1 = int(square_str1)
        proiz = square0 * square1
        proiz_str = str(proiz)
        mid_index = len(proiz_str) // 2
        # Извлекаем 4 цифры из середины
        R_next = "0." + proiz_str[mid_index - 2 : mid_index + 2]
        random_numbers.append(float(R_next))  # Преобразуем обратно в float для удобства
        R0 = R1
        R1 = R_next
    return random_numbers

R0 = 0.5836
R1 = 0.2176
N = 6

print(Neiman(R0, R1, N))