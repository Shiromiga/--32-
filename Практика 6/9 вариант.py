#9 варинат
#1 задание 

a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9, 10, 11, 12]
print(a, b)
a,b = b,a
print(a, b)


#2 задание
spisok = input()
s = spisok.split()
minn = 1000
e = [int(x) for x in s]
for i in range(len(e)):
    if abs(e[i]) < minn:
        minn = e[i]
s.reverse()
print(minn, print(s))
