

s = input()
s_lst = s.split()

tp = tuple(tuple(map(tuple, (s.split('=') for s in s_lst))))
tp1 = tuple(map(lambda x: tuple(x.split("=")), s_lst))
print(tp,'\n',tp1)