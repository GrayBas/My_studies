# Объявите функцию с именем str_min, которая сравнивает
# две переданные строки и возвращает минимальную из них
# (то есть, выполняется лексикографическое сравнение строк).
# Затем, используя функциональный подход к программированию
# (то есть, более сложные функции реализуются путем вызова более простых),
# реализовать еще две аналогичные функции:

# - с именем str_min3 для поиска минимальной строки из трех переданных строк;
# - с именем str_min4 для поиска минимальной строки из четырех переданных строк.


# берём нужные имена функций и каскадным
# присваиванием связываем с встроенной функцией min
str_min = str_min3 = str_min4 = min


# --------сравнение через функции min------------------------------------------------


# def str_min(*args2):
#     return min(args2)
#
#
# def str_min3(*args3):
#     return min(args3[0], str_min(*args3[1:]))
#
#
# def str_min4(*args4):
#     return min(args4[0], str_min3(*args4[1:]))

# -----сравнение через функции min----------------------------------------------------

# def str_min(*args2):
#     return min(args2)
#
#
# def str_min3(*args3):
#     return str_min(args3[0], str_min(*args3[1:]))
#
#
# def str_min4(*args4):
#     return str_min(args4[0], str_min3(*args4[1:]))


# --решение путем сравнения операторами-------------------------------------------------------------

# def str_min(*args2):
#     return args2[0] if args2[0] < args2[1] else args2[1]
#
#
# def str_min3(*args3):
#     min2 = str_min(*args3[1:])
#     return args3[0] if args3[0] < min2 else min2
#
#
# def str_min4(*args4):
#     min3 = str_min3(*args4[1:])
#     return args4[0] if args4[0] < min3 else min3

print('min of 2 string', str_min(*input().split()))
print('min of 3 string', str_min3(*input().split()))
print('min of 4 string', str_min4(*input().split()))
