n = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [5, 4, 3]]

lst = [[j[i] for j in n] for i in range(len(n[0]))]

print(lst)