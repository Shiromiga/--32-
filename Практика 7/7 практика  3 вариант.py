#7 практика Варинат 3



# 1 Задание
import math
def f(x, y):
    return math.sqrt(x ** 2 + y ** 2) # Формула для нахождения гипотенузы

st1, str1 = map(int, input('Катеты 1 треугольника st1,str1 = ').split())
st2, str2 = map(int, input('Катеты 2 треугольника st2, str2 = ').split())
ca1 = f(st1, str1)
ca2 = f(st1, str2)
if ca1 == ca2:
    print('Гипотенузы равны')
if ca1 > ca2:
    print('Гипотенуза 1 треугольника больше')
if ca1 < ca2:
    print('Гипотенуза 2 треугольника больше')


# Задание 2
e = input('').lower().split(' ')
for i in range(len(e)):
    e[i] = ''.join(sorted(e[i])) # меняет букву на отсортированную 
print(' '.join(e))
