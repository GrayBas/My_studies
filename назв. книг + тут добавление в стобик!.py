import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
#lst_in = ['Евгений Онегин', 'Муму', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
n = 0
while len(lst_in) > n:
    if ' ' in lst_in[n]:
        lst_in.pop(n)
        n -= 1
    n += 1
print(*lst_in)