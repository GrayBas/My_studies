# Сортировка пузырьком - это метод сортировки массивов
# и списков путем последовательного сравнения и обмена
# соседних элементов, если предшествующий оказывается больше
# последующего (при сортировке по возрастанию).
#Вводится список целых чисел в одну строку через пробел.
# Необходимо выполнить его сортировку по возрастанию (неубыванию)
# методом всплывающего пузырька
#

a = list(map(int, input().split()))
#a = [7, 2, 6, 1]
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)


#_________________________________-https://younglinux.info/algorithm/bubble
i = 0
while i < len(a) - 1:
    j = 0
    while j < len(a) - 1 - i:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i += 1

print(a)

#________ с помощью True False
# for i in range(len(lst), 0, -1):
#     ordered = True
#     for j in range(1, i):
#         if lst[j - 1] > lst[j]: # пока стравнение проходит ordered будет false
#
#             lst[j - 1], lst[j], ordered = lst[j], lst[j - 1], False
#     if ordered: break
# print(*lst)