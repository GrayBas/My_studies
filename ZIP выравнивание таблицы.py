import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = [list(map(int, l.split())) for l in lst_in]
z = zip(*zip(*lst))

try:
    while True:
        print(*next(z))
except StopIteration:
    pass

