def lenth6(a):
    return a, len(a)


#d = {key: value for key, value in [lenth6(i) for i in list(input().split())]}
d = dict(lenth6(i) for i in input().split())
a = sorted(d, key=lambda x: d[x])
print(*a)