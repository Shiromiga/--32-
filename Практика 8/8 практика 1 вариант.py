# 1 вариант


#1 адание
import random

N = 5  # размерность матрицы
# создание матрицы и заполнение случайными числами
A = [[random.randint(-10, 10) for j in range(N)] for i in range(N)]
print("Матрица A:")
for i in range(N):
    for j in range(N):
        print(A[i][j], end=" ")
    print()

# вычисление суммы и количества положительных элементов над главной диагональю
sum_positive = 0
count_positive = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i][j] > 0:
            sum_positive += A[i][j]
            count_positive += 1

# вывод результата
print("Сумма положительных элементов над главной диагональю:", sum_positive)
print("Количество положительных элементов над главной диагональю:", count_positive)








#2 Задание
import random

N = 5  # количество строк матрицы
M = 4  # количество столбцов матрицы
# создание матрицы и заполнение случайными числами
B = [[random.randint(-10, 10) for j in range(M)] for i in range(N)]
print("Матрица B:")
for i in range(N):
    for j in range(M):
        print(B[i][j], end=" ")
    print()


for i in range(N):
    max_element = max(B[i])
    min_element = min(B[i])

    # нахождение индексов максимального и минимального элементов в строке
    max_index = B[i].index(max_element)
    min_index = B[i].index(min_element)

    # обмен максимального элемента с первым элементом строки
    B[i][0], B[i][max_index] = B[i][max_index], B[i][0]

    # обмен минимального элемента с последним элементом строки
    B[i][-1], B[i][min_index] = B[i][min_index], B[i][-1]


print("Измененная матрица B:")
for i in range(N):
    for j in range(M):
        print(B[i][j], end=" ")
    print()
