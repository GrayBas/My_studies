#sp = ['Москва', 'Уфа', 'Тула', 'Самара', 'Омск', 'Воронеж','Владивосток', 'Лондон', 'Калининград', 'Севастополь']

#z = zip(*[iter(input().split())]*3)
#print(*z)

st = iter(input().split())

for i in zip(st, st,st):
    print(*i)