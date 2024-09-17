lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
#print(lst_in)
s = []
d = {}
#d = [[int(key), value] for key, value in [m.split('=') for m in lst_in]]
for x in range(len(lst_in)):
    s += lst_in[x].split('=')
#print(d)

for x in range(0,len(s),2):
    d[int(s[x])] = s[x+1]
print(*sorted(d.items()))
#print(s)

#------------------------------------
lst = [i.split('=') for i in lst_in]
d = {int(i): v for i, v in lst} # генератор словарей
print(*sorted(d.items()))

#---------------
d = {int(x.split('=')[0]):x.split('=')[1] for x in lst_in}
print(*sorted(d.items()))