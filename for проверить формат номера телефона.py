n = input()
z = '+7(xxx)xxx-xx-xx'
ans = 'НЕТ'
if len(n) != len(z) or n[0:2] != '+7':
    print(ans)
else:
    for i, b in enumerate(n):
        if z[i] != 'x':
            if z[i] == b:
                ans = 'ДА'
            else:
                ans = 'НЕТ'
                break
        if z[i] == 'x':
            if b.isdigit():
                ans = 'ДА'
            else:
                ans = 'НЕТ'
                break
    print(ans)

#------------------------------------------

s = '+7(xxx)xxx-xx-xx'
num = input()
count = 0
if len(s) == len(num):
    for i, item in enumerate(num):
        if s[i] == item or s[i] == 'x' and item.isdigit():
            count += 1

print('ДА' if count == 16 else 'НЕТ')