#Вводится натуральное число N. С помощью list comprehension
# сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы.
# (Главная диагональ - это элементы, идущие по диагонали
# от верхнего левого угла матрицы до ее нижнего правого угла).
# Результат вывести в виде таблицы чисел как показано в примере ниже.

n = int(input())

lst = [[0] * n for x in range(n) ]
for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            lst[i][j] = 1

for a in lst:
    print(* a)

#--------------------------
n = int(input())

lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

for i in lst:
    print(*i)

#----------------------------------------
n = int(input())
mtx = [[int(i == j) for j in range(n)] for i in range(n)]
for row in mtx:
    print(*row)