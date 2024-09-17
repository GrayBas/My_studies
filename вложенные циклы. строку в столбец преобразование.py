a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        a[i][j], a[j][i] = a[j][i], a[i][j]
print(*a, sep='\n')