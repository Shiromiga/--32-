#7 практика 9 вариант
#1
s = int(input())
k = 0
while s > 0:#Пока число не 0
    summ = sum(int(x) for x in str(s))#Сумма цифр числа
    s -= summ
    k +=1
print("Задание 1. Число преобразуется в 0 за " + str(k)+ " ходов")
#2
def e(x):
    sum = 0
    product = 1
    for num in x:
        sum += num
        product *= num # Произведение эллементов массива
    average = sum / len(x) #Среднее значение

    return average, product
f = [1, 2, 3, 4, 5]
g = [2, 4, 5, 6, 8]
l = [5, 9, 8, 1, 2]
print("Задание 2. Среднее арифмитическое и произведение элементов 3 массивов" + str(e(f))+ str(e(g))+ str(e(l)))
