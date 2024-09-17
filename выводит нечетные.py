n, m = map(int, input().split())

while n < m-1:
    while n % 2 == 0 :
        n += 1
        print(n, end=' ')
    n += 2
    print(n, end=' ')