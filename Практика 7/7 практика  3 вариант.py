#Варинат 3
# 1 Задание
import math
def gipotenuza(x, y):
    return math.sqrt(x ** 2 + y ** 2)  # вычисляем гипотенузу

st1, str1 = map(int, input('Катеты 1-го треугольника st1,str1 = ').split())
st2, str2 = map(int, input('Катеты 2-го треугольника st2, str2 = ').split())
ca1 = gipotenuza(st1, str1)
ca2 = gipotenuza(st1, str2)
if ca1 == ca2:
    print('Гипотенузы равны')
if ca1 > ca2:
    print('Гипотенуза 1-го треугольника больше')
if ca1 < ca2:
    print('Гипотенуза 2-го треугольника больше')


# Задание 2
e = input('').lower().split(' ')
for i in range(len(e)):
    e[i] = ''.join(sorted(e[i]))
print(' '.join(e))
