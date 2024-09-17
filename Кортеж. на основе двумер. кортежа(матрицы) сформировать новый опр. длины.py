t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
n = int(input())
t2 = ()
for x in t[:n]:
    t2 += (x[:n],)
[print(*x) for x in t2]
#------------------------

t3 = tuple(t[i][:n] for i in range(n))
[print(*x) for x in t3]