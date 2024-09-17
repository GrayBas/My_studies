t = tuple(map(int, input().split()))
c = ()
for x in t:
    if x not in c:
        c += (x,)
print(*c)

#----------------------------------------------
e = tuple(map(int, input().split()))
d = dict.fromkeys(e)
d = tuple(d.keys())
print(*d)