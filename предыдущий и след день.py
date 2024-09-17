a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, n = map(int, input().split())            # вводим месяц и день
if a[m-1] - n == 0:
    print(f'{m:02}.{n-1:02} {m+1:02}.{a[m]*0+1:02}')
elif a[m-1] > n > 1:
    print(f'{m:02}.{n-1:02} {m:02}.{n+1:02}')
elif n == 1:
    print(f'{m-1:02}.{a[m-2]:02} {m:02}.{n+1:02}')
else:
    if n > a[m-1]:
        print('wrong day')

