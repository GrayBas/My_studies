a = list(map(int, input().split()))

for i in range(0, len(a)*2, 2):
    a.insert(i, a[i])
print(*a)