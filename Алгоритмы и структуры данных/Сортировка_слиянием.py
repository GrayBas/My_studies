def merge(a:list, b:list) -> list:
    """ Слияние отсортированных массивов 'a' и 'b'"""
    c = []
    i = k = 0                           # инициализируем курсоры для прохода по спискам
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:                # если эл-т из списка "а" меньше либо равен чем эл-т
            c.append(a[i])              # из списка "b" то добавляем его в список "с"
            i += 1                      # увеличиваем курсор списка "а" на 1
        else:                           # эл-т из списка "b" меньше чем эл-т и списка "а"
            c.append(b[k])              # добавляем его в список "с"
            k += 1                      # увеличиваем курсор списка "b" на 1
    if i < len(a):                  # если цикл завершился, и в списке "а" остались элементы
        c += a[i:]                  # то добавляем их в список "с" срезом
    if k < len(b):                  # если цикл завершился, и в списке "b" остались элементы
        c += b[k:]                  # то добавляем их в список "с" срезом
    return c
        
# a = [1, 5, 6, 7, 23, 7888]
# b = [1, 2, 3, 4, 5, 6, 9]
# print(merge(a, b))


def merge_sort(a:list) -> list:
    """ Разделение массива 'a' на две части передача их для сортировки и слияния 
        в функцию merge
    """
    if len(a) <= 1:                 
        return a
    middle = len(a) // 2            # находим серидину массива
    left = merge_sort(a[:middle])   # делим список на две части, каждый раз доходя 
    right = merge_sort(a[middle:])  # рекурсией до базового случая
    return merge(left, right)



print(merge_sort([2, 65, 7, 45, 1, 3, 2, 8, 65, 14, 25, 56, 17,
                  0, 10, 12, 13, 14, 15, 99, 54, 77]))
print(merge_sort([2, 65, 7, 45, 1, 3]))
print(merge_sort([]))
print(merge_sort([2]))




# def merge(left:list, right:list):
#     lst = [0] * (len(left) + len(right))
#     i = j = n = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             lst[n] = left[i]
#             i += 1
#             n += 1
#         else:
#             lst[n] = right[j]
#             j += 1
#             n += 1
#     while i < len(left):
#         lst[n] = left[i]
#         i += 1
#         n +=1
#     while j < len(right):
#         lst[n] = right[j]
#         j += 1
#         n += 1
#     return lst


# def merge_sort(a:list):
#     if len(a) <= 1:
#         return a
#     middle = len(a) // 2
#     left = [a[i] for i in range(0, middle)]
#     right = [a[i] for i in range(middle, len(a))]
#     return merge(left, right)


# print(merge_sort([2, 65, 7, 45, 1, 3, 2, 8, 65, 14, 25, 56, 17,
#                   0, 10, 12, 13, 14, 15, 99, 54, 77]))
# print(merge_sort([2, 65, 7, 45, 1, 3]))
# print(merge_sort([]))
# print(merge_sort([2]))
