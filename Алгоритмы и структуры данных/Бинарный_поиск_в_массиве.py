def binary_search_recursive(lst, key, left: int = 0, right: int = -1) -> bool:
    """ Бинарный поиск в рекурсивной интерпретации.
        Возвращает True если эл-т найден и False если нет.
    """
    if right < 0:
        right = len(lst) - 1
    if right < left:
        return False
    
    middle = (right + left) // 2
    
    if lst[middle] == key:
        return True
    elif lst[middle] < key:
        return binary_search_recursive(lst, key, left + 1, right)
    else:
        return binary_search_recursive(lst, key, left, right - 1)
        

print(binary_search_recursive([1,2,3,4,6,7,9,23,45,96], 6))
print(binary_search_recursive([1,1,1,1,1,1,2,2,2,3,4,6,7,7,7,9,9,9,9,9,9,23,45,45,45,45,45,96], 45))
print(binary_search_recursive([2], 4))
print(binary_search_recursive([4], 4))
print(binary_search_recursive([], 4))


def binary_search_iterative(lst: list, key) -> bool:
    left = 0
    right = len(lst) - 1
    while right >= left:
        middle = (left + right) // 2
        if lst[middle] == key:
            return True
        elif lst[middle] < key:
            left = middle + 1
        else:
            right = middle - 1
    return False


print(binary_search_iterative([1,2,3,4,6,7,9,23,45,96], 45))
print(binary_search_iterative([1,1,1,1,1,1,2,2,2,3,4,6,7,7,7,9,9,9,9,9,9,23,45,45,45,45,45,96], 7))
print(binary_search_iterative([2], 4))
print(binary_search_iterative([4], 4))
print(binary_search_iterative([], 4))
            

""" Бинарный поиск в иттеративной интерпретации. Данный бинарный поиск
    находит позиции в пределах которых находится искомый эл-т, т.к. искомого
    эл-та в массиве может быть больше 1-го.     
"""
def left_bound(a: list, key) -> int:
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (right + left) // 2
        if a[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(a: list, key) -> int:
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (right + left) // 2
        if a[middle] <= key:
            left = middle
        else:
            right = middle
    return right


def binary_search_interval_iterative(a: list, key) -> bool:
    return right_bound(a, key) - left_bound(a, key) > 1


print(binary_search_interval_iterative([1,2,3,4,6,7,9,23,45,96], 4))
print(binary_search_interval_iterative([1,1,1,1,1,1,2,2,2,3,4,6,7,7,7,9,9,9,9,9,9,23,45,45,45,45,45,96], 7))
print(binary_search_interval_iterative([2], 4))
print(binary_search_interval_iterative([4], 4))
print(binary_search_interval_iterative([], 4))