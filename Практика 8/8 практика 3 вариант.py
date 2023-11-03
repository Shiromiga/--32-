# Вариант 9


# Задание 1
def symetrich(m):
    n = len(m)

    #Проверяем каждый элемент матрицы
    for i in range(n):
        for j in range(n):
             Если элементы не совпадают относительно главной диагонали, возвращаем False
            if m[i][j] != m[j][i]:
                return False

    # Если все элементы совпадают относительно главной диагонали, возвращаем True
    return True


# Пример использования программы
m = [[1, 2, 3],
     #[2, 4, 5],
     #[3, 5, 6]]

if symetrich(m):
    print("Матрица является симметричной")
else:
    print("Матрица не является симметричной")



#Задание 2
def m(matrix):
    n = len(matrix) # Количетсво строк
    m = len(matrix[0]) # Количество столбцов

    # Находим индексы наибольшего элемента в матрице
    max_element = matrix[0][0]
    max_ix = 0 #Строки 
    max_j = 0 #Столбцы

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_i = i #Индексы макс эллементов
                max_j = j #Индексы макс эллементов

    # Переставляем строки и столбцы так, чтобы наибольший элемент оказался в верхнем левом углу
    matrix[0], matrix[max_i] = matrix[max_i], matrix[0]

    for i in range(n):
        matrix[i][0], matrix[i][max_j] = matrix[i][max_j], matrix[i][0]

    return matrix


matrix = [[1.2, 2.4, 0.8],
          [4.5, 3.1, 2.7],
          [0.9, 5.6, 3.9]]

m = m(matrix)

print("Итоговая матрица:")
for r in m:
    print(r)
