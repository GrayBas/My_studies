import random

random.seed(1)

#N = int(input())
N = 7
P = [[0] * N for i in range(N)]



s = 0

while s != 10:
    r = random.randint(0, len(P)-1)
    x = random.randint(0, len(P)-1)
    if r == 0 and 0 < x < len(P)-1:
        if sum([P[r][x], P[r][x + 1], P[r + 1][x], P[r + 1][x + 1], P[r][x-1], P[r+1][x-1]])==0:
            P[r][x] = 1
            s += 1
        else:
            continue

    if r == 0 and x == len(P)-1:
        if sum([P[r][x], P[r + 1][x], P[r][x-1], P[r+1][x-1]])==0:
            P[r][x] = 1
            s += 1
        else:
            continue

    if r == 0 and x == 0:
        if sum([P[r][x], P[r + 1][x], P[r][x-1], P[r+1][x+1]])==0:
            P[r][x] = 1
            s += 1
        else:
            continue

    if r == len(P)-1 and 0 < x < len(P)-1:
        if sum([P[r][x], P[r][x + 1], P[r][x-1], P[r-1][x+1], P[r-1][x], P[-1][x-1]])==0:
            P[r][x] = 1
            s += 1
        else:
            continue

    if r == len(P)-1 and x == len(P)-1:
        if sum([P[r][x], P[r][x-1], P[r-1][x], P[-1][x-1]])==0:
            P[r][x] = 1
            s += 1
        else:
            continue

    if r == len(P)-1 and x == 0:
        if sum([P[r][x], P[r][x + 1], P[r-1][x+1], P[r-1][x]])==0:
            P[r][x] = 1
            s += 1
        else:
            continue

    if 0 < r < len(P)-1 and 0 < x < len(P)-1:
        if sum([P[r][x], P[r][x + 1], P[r + 1][x], P[r + 1][x + 1],
        P[r][x - 1], P[r - 1][x], P[r - 1][x - 1], P[r - 1][x + 1], P[r + 1][x - 1]]) == 0:
            P[r][x] = 1
            s += 1
        else:
            continue

print(*P,  len(P), sep='\n')