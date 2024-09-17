# Трегольник паскаля
n = 50
p = []

for i in range(n):
    row = [1] * (i+1) # создаем список длиной i+1
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = p[i-1][j-1] + p[i-1][j] # в предыдущей строке складываем
            #числа и записыввем в нижнюю ячейку на след строке

    p.append(row)

for r in p:
    print(r)