import time


def get_nod(a, b):
    # """Вычисляется НОД для натуральных чисел a и b
    #     по алгоритму Евклида.
    #     Возвращает вычисленный НОД.
    # """
    # while a != b:
    #     if a > b:
    #         a -= b
    #     else:
    #         b -= a
    """Вычисляется НОД для натуральных чисел a и b
            по быстрому алгоритму Евклида.
            Возвращает вычисленный НОД.
        """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


res = get_nod(18, 24)
print(res)
help(get_nod)


def test_nod(func):
    # -- тест №1 на правильность вычислений---------------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('#test1 - ok')
    else:
        print("#test1 - fail")

    # -- тест №2 на правильность вычислений---------------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    # -- тест №3 на скорость работы---------------------
    a = 2
    b = 100000000

    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


test_nod(get_nod)