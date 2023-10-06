s = 'еж ел еду'
cnt = 0
for word in s.split(' '):
    if word.strip()[0] == 'е':
        cnt += 1
print(cnt)
