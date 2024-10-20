from string import ascii_lowercase, ascii_uppercase
import random

chars = ascii_lowercase + ascii_uppercase


def decorator(func):
    def wrapper(n):
        return f"{next(func(n))}@mail.ru"
    return wrapper


@decorator
def get_mail(max_size):
    while True:
       yield ''.join(chars[random.randint(0, len(chars)-1)] for i in range(max_size))


length_m = int(input())
for i in range(5):
    print(get_mail(length_m))


