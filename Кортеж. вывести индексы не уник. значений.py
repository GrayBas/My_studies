t = tuple(map(int, input().split()))
print(*(x for x, y in enumerate(t) if t.count(y) > 1))

#--------------------

tpl  = tuple(map(int, input().split()))
d = {}
for e in tpl:
    d[e] = d.get(e, 0) + 1  #добавляем в словарь значения(ключ) и их повторения(значю) в кортеже

print(*(i for i, n in enumerate(tpl) if d[n] > 1))# если значение в словаре больше 1 то выводим