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
with open('ИгнатьевДмитрийСергеевич_УБ-32_vvod(8.1).txt', 'r') as f:
    e = f.readlines()
    matrix = []
    for A in e:
        A = A.strip().split()
        A = [int(x) for x in A]
        matrix.append(A)
result1, result2 = mat(matrix)



#2 Задание
with open('ИгнатьевДмитрийСергеевич_УБ-32_vvod(8.1).txt', 'r') as f:
    e = f.readlines()
    matrix = []
    for A in e:
        A = A.strip().split()
        A = [int(x) for x in A]
        matrix.append(A)
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
with open('ИгнатьевДмитрийСергеевич_УБ-32_vivod(8.6).txt.txt', 'w') as vihod:
    res = str(result1)
    res2 = str(result2)
    vihod.write('Задание 1)')
    vihod.write(' ')
    vihod.write(res2)
    vihod.write('  ')
    vihod.write('Задание 2)')
    vihod.write(' ')
    vihod.write(res2)
    vihod.write('\n')
    for i in range(len(r)):
        for j in range(len(r)):
            vihod.write(str(matrix[i][j]))
            vihod.write(' ')
        vihod.write('\n')
        vihod.write('\n')
        
