from functools import wraps


def df_decorator(tag="h1"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            #wrapper.__name__ = func.__name__
            #wrapper.__doc__ = func.__doc__

            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapper
    return decorator


@df_decorator(tag="div")
def low_register(string:str):
    """Функция переводит все буквы верхнего регистра в нижний"""
    return string.lower()

s = input()

print(low_register(s),"\n",low_register.__name__,"\n",low_register.__doc__)