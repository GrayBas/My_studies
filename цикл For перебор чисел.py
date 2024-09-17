a = map(int, input().split())
lst = list(a)
b = 0
for i in range(len(lst)):
    if lst[i] % 2 != 0:

        b += lst[i]

print(b)


#--------перебирает список напрямую----------------------------------

print(sum([i for i in map(int,input().split()) if i % 2 != 0])

#-----------------------------------------------

lst = list(map(int, input().split()))
summ = 0

for i in lst:
    if i % 2 == 1:
        summ += i

print(summ)