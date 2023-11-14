#Вариант 3

#Задание 1
s = [1, 2, 6, 4, 9, 10, 11, 12, 13, 14]
summ = 0 
for i in range(len(s)):
    if i%2==0:
       summ+=s[i]
print(s, summ)

#Задание 2
e = [1, 2, 3, 4, 5, 6, 7, 15, 16, 21]
for i in range(len(e)):
    if e[i] < 15:
        e[i] = e[i]*2 # Удвоение эллемента, если он меньше 15
print(e)
