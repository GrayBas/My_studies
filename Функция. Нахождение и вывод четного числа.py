def is_even(n):
    return not n % 2


n = int(input())

while n != 1:
    if is_even(n):
        print(n)
    n = int(input())


# ------------

def func(x):
    return int(x) % 2


for i in iter(input, '1'):
    if not func(i):
        print(i)
