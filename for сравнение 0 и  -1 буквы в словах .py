n = list(input().lower().split())
ans = 'ДА'
lst = ['ь', 'ъ', 'ы']
for i in range(len(n)-1): #-1 для того чтобы перебор не брал последнее слово т.к. его нескем сравнивать
    if n[i][-1] in lst:
        if n[i][-2] != n[i+1][0]:
            ans = "НЕТ"
            break
    else:
        if n[i][-1] != n[i+1][0]:
            ans = 'НЕТ'
            break

print(ans)

