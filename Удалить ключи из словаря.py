# Вводятся данные в формате ключ=значение в одну строчку
# через пробел. Необходимо на их основе создать словарь d,
# затем удалить из этого словаря ключи 'False' и '3',
# если они существуют. Ключами и значениями словаря являются строки.
# Вывести полученный словарь на экран командой:

#d = dict([[key, value] for key, value in
  #  [s.split('=') for s in input().split()]])
d = dict([i.split('=') for i in input().split()])

#print(d)

if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']
#print(d)
print(*sorted(d.items()))