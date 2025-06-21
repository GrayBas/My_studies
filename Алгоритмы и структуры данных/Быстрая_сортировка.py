import random


def quicksort(s:list):
    """ Реализация быстрой сортировки массива 's' """
    if len(s) <= 1:                                         # крайний случай, пустой массив или с одним эл-том считается отсортированы 
        return s
    q = random.choice(s)                                    # задаем опорный эл-т который будет разделять эл-ты на те которые меньше, больше или равны ему
    left = list(filter(lambda x: x < q, s))                 # создаём массив с эл-ми меньше 'q'
    middle = [i for i in s if i == q]                       # создаём массив с эл-ми равными 'q'                       
    right = list(filter(lambda x: x > q, s))                # создаём массив с эл-ми больше 'q'
    
    return quicksort(left) + middle + quicksort(right)      # рекурсивно раделяем список до базового случая параллельно сортируя начиная с левой части
                                                            # при завершении каждой рекурсии конкатенируем полученные списки


print(quicksort([2, 65, 7, 45, 1, 3, 2, 8, 65, 14, 25, 56, 17, 0, 10, 12, 13, 14, 15, 99, 54, 77]))
print(quicksort([2, 65, 7, 45, 1, 3]))
print(quicksort([]))
print(quicksort([2]))


def QuickSort(a: list):
    """ Реализация быстрой сортировки массива 'a' """    
    if len(a) <= 1:
        return a
    
    q = random.choice(a)
    left = []
    middle = []
    right = []
    for elem in a:
        if elem < q:
            left.append(elem) 
        elif elem > q: 
            right.append(elem) 
        else: 
            middle.append(elem)
    return QuickSort(left) + middle + QuickSort(right)
    
    
print(QuickSort([2, 65, 7, 45, 1, 3, 2, 8, 65, 14, 25, 56, 17, 0, 10, 12, 13, 14, 15, 99, 54, 77]))
print(QuickSort([2, 65, 7, 45, 1, 3]))
print(QuickSort([]))
print(QuickSort([2]))


