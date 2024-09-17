lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']
t = ()
for z in range(len(lst_in)):
    c = tuple(lst_in[z].split())
    t += (c,)
print(t)

#---------------------------
x = tuple(tuple(y.split()) for y in lst_in)
#------------------------------------
tup = ()
for i in lst_in:
    tup += tuple(i.split()),
print(tup)