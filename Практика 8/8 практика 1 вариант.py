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
matrix = [
    [31, 2, 100, 102],
    [14, 5, 61, 1004],
    [9, 8, 30, 322],
    [3, 5,30,222]]
for r in matrix:
        max_idx = 0
        for i in range(1, len(r)):
            if r[i] > r[max_idx]:
                max_idx = i
        r[0], r[max_idx] = r[max_idx], r[0]
        min_idx = 0
        for i in range(1, len(r)):
            if r[i] < r[min_idx]:
                min_idx = i
        r[-1], r[min_idx] = r[min_idx], r[-1]


print(matrix)
