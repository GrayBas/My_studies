#Tребуется расставить на поле P случайным образом
# M = 10 единиц (целочисленных) так, чтобы они не соприкасались друг с другом
import random
random.seed(1)

N = int(input())
P = [[0] * N for i in range(N)]
s = 0
while s != 10:
    r, c = random.randint(0, N - 1), random.randint(0, N - 1)
    if not sum(P[i][y] for i in range(max(0, r - 1), min(r + 2, N))
                        for y in range(max(0, c - 1), min(c + 2, N))):
        P[r][c] = 1
        s += 1


print(*P, sep='\n')