# Вариант 9


# Задание 1
def symetrich(m):
    n = len(m)

    #Проверяем каждый элемент матрицы
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False

    # Если все элементы совпадают относительно главной диагонали, возвращаем True
    return True


with open('ИгнатьевДмитрийСергеевич_УБ-32_vvod(8.1).txt', 'r') as f:
    e = f.readlines()
    matri = []
    for A in e:
        A = A.strip().split()
        A = [int(x) for x in A]
        matri.append(A)
#Задание 2
def mn(matrix):
    global n,m
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

with open('ИгнатьевДмитрийСергеевич_УБ-32_vvod(8.1).txt', 'r') as f:
    a = f.readlines()
    matrix = []
    for A in a:
        A = A.strip().split()
        A = [int(x) for x in A]
        matrix.append(A)
    e = mn(matrix)
    print(e)
    with open('ИгнатьевДмитрийСергеевич_УБ-32_vivod(8.7).txt.txt', 'w') as vihod:
        vihod.write("Задание 1)")
        if symetrich(matri):
            vihod.write("Матрица симметрична")
        else:
            vihod.write("Матрица не является симметричной")
        vihod.write('\n')
        vihod.write("Задание 2)")
        vihod.write("\n")
        for i in range(n):
            for j in range(m):
                vihod.write(str(e[i][j]))
                vihod.write(' ')
            vihod.write('\n')
