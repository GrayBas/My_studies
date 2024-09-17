#Вводится таблица целых чисел (см. пример ниже) размером
# N x N элементов (N определяется по входным данным).
# Эта таблица содержит нули, но кое-где - единицы.
# С помощью функции с именем verify, на вход которой
# передается двумерный список чисел, необходимо проверить,
# являются ли единицы изолированными друг от друга, то есть,
# вокруг каждой единицы должны быть нули.

# Рекомендуется следующий алгоритм. В функции verify производить
# перебор двумерного списка. Для каждого элемента (списка) со значением 1
# вызывать еще одну вспомогательную функцию is_isolate для проверки
# изолированности единицы. То есть, функция is_isolate должна возвращать True,
# если единица изолирована и False - в противном случае.
#
# Как только встречается не изолированная единица, функция verify должна
# возвращать False. Если успешно доходим (по элементам списка) до конца,
# то возвращается значение True.

#Решение путем расширения матрицы, но лишь с двух сторон
def verify(n):
    n_add = n
    n_add.append([0]*(len(n)))
    for i in n:
        i.append(0)
    print(*n_add, sep='\n')
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i][j] == 1:
                if not is_isolate(n[i][j], n[i][j + 1], n[i + 1][j], n[i + 1][j + 1]):
                    return False

    return True


def is_isolate(*args):
    return sum(args) <= 1


#Решение путем расширения матрицы нулями
# def verify(lst):
#     #расширяю матрицу нулями, чтобы не искать граничные индексы
#     lst.insert(0, [0] * len(lst))
#     lst.append([0] * (len(lst)-1))
#     for li in lst:
#         li.insert(0, 0)
#         li.append(0)
#     #ищу
#     for i, li in enumerate(lst):
#         if sum(li) > 0:
#             for j, nj in enumerate(li):
#                 if nj == 1:
#                     if not is_isolat(i,j,lst):
#                         return False
#     return True
#
#
#
# def is_isolat(i1, j1, lst):
#     sm = sum([sum(l[j1-1:j1+2]) for l in lst[i1-1:i1+2]])
#     return True if sm == 1 else False



#Решение путем расширения матрицы нулями
# def is_isolate(lst, i, j):
#     n = [0, 1]
#     return sum([lst[i + k][j + l] for k in n for l in n]) == 1
#
#
# def verify(lst_in):
#     n = len(lst_in)
#     lst = [[0 for i in range(n + 2)] for j in range(n + 2)]
#     print(*lst, sep='\n')
#     for i in range(n):
#         for j in range(n):
#             lst[i + 1][j + 1] = lst_in[i][j]
#     print('новая матрица', *lst, sep='\n')
#
#     for i in range(n + 2):
#         for j in range(n + 2):
#             if lst[i][j] == 1 and not is_isolate(lst, i, j):
#                 return False
#     return True

print(verify([[1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0]]))
