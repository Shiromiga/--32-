n = int(input('Введите длину ряда: '))
f1 = f2 = 1
su = 0
i = 2
while i < n:
    f1, f2 = f2, f1 + f2
    su+=f2
    i += 1
print(su+2)
