from functools import wraps

def df_decorator(start=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #wrapper.__name__ = func.__name__ # Тоже самое что и декоратор @wraps
            #wrapper.__doc__ = func.__doc__

            return func(*args) + start

        return wrapper
    return decorator

@df_decorator(start=5)
def summ(stroka: str):
    """Функция преобразует строку из чисел в список и суммирует их"""
    lst = list(map(int, stroka.split()))
    return sum(lst)

n = input()

print(summ(n),"\n",summ.__doc__,"\n",summ.__name__ )