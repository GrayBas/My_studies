#Вводятся данные в формате ключ=значение в одну строчку
# через пробел. Значениями здесь являются целые числа (см. пример ниже).
# Необходимо на их основе создать словарь d с помощью функции dict()
# и вывести его на экран командой: print(*sorted(d.items()))
# one=1 two=2 three=3
s = input().split()

#print(s, type(s))
r = []
for i in range(len(s)):
    r += [s[i].split('=')]

d = dict(r)
for x in d:
    d[x] = int(d[x])
#print(d)
print(*sorted(d.items()))


#-------------------------------------------
d = dict(c.split('=') for c in input().split())
for c in d:
  d[c] = int(d[c])
print(*sorted(d.items()))

#--------------------------------------
d = dict([[key, int(value)] for key, value in [s.split('=') for s in  input().split()]])