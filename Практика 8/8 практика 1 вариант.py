# 8 практика 1 вариант


#1 Задание
def mat(matrix):
    n = len(matrix)
    summ = 0
    count = 0

    for i in range(n): # Количество элементов в матрице 
        for j in range(i+1, n): # Берем элемент выше главной дивгонали 
            if matrix[i][j] > 0:
                summ+= matrix[i][j]
                count += 1

    return summ, count
A = [
    [1, -3, 5],
    [3, 5, -8],
    [-1, 9, 9]]
result1, result2 = mat(A)
print("Сумма положительных эллементов", result1)
print("Количество таких элементов", result2)



#2 Задание
def izmena(matrix):
    for r in matrix:
        min_idx = 0
        max_idx = 0

        # Находим индексы минимального и максимального элементов в строке
        for i in range(1, len(r)):
            if r[i] < r[min_idx]:
                min_idx = i
            if r[i] > r[max_idx]:
                max_idx = i

        # Меняем местами минимальный элемент с оследним, а максимальный элемент с первым
        r[0], r[max_idx] = r[max_idx], r[0]
        r[-1], r[min_idx] = r[min_idx], r[-1]

    return matrix


B = [
    [31, 2, 100],
    [14, 5, 61],
    [9, 8, 10]]

result = izmena(B)
print(result)
