def chec_sorted(a:list, ascending=True):
    """ Проверка отсортированности за O(len(a)).
        ascending = True - проверка на упорядоченность по возрастанию
        ascending = False - проверка на упорядоченность по убыванию
    """
    flag = True
    s = 2 * ascending - 1           # True и False можно представить как 1 и 0. Чтобы проверить массив
    for i in range(0, len(a)-1):    # на упорядоченность по убыванию домнажаем эл-ты на -1
        if s * a[i] > s * a[i+1]:
            flag = False
            break
    return flag
    
     
print(chec_sorted([1,2,3,4,5,6,7]))
print(chec_sorted([7,6,5,4,3,2,1,0], ascending=False))
print(chec_sorted([6,8,45,98,3]))