a = input().split()
lst = list(a)
for i in range(len(lst)):
    lst[i] = len(lst[i])
print(*lst)

#--------------------

print(*map(len, input().split()))