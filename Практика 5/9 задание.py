text = input().split(' ')
c = 0
word = 'da'
for i in text:
    if i == word:
        c+=1
print("Количество слов " + word + " " +  str(c))
