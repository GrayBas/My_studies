#В виде строки записано арифметическое выражение, например:
#"10 + 25 - 12" или "10 + 25 - 12 + 20 - 1 + 3"
#и т. д. То есть, количество действий может быть разным.
#Необходимо выполнить вычисление и результат отобразить на экране.
#Полагается, что в качестве арифметических операций здесь используется
#только сложение (+) и вычитание (-), а в качестве операндов - целые неотрицательные числа.
#Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

text = input().replace(' ', '').replace('-', '+-').split('+')
print(sum(map(int, text)))



#-----------------------------------------\
exp = input().replace(' ', '')
summ = 0

for val in exp.split('+'):
    for i, v in enumerate(val.split('-')):
        if i == 0:
            summ += int(v)
        else:
            summ -= int(v)

print(summ)

#--------------------------------------------

oper=input().replace('+',' + ').replace('-',' - ').split()
s=oper[0]
for i,v in enumerate(oper):
    if i==0 and oper[0] == '-':
        s = int(oper[1]) * (-1)
    elif i == 0 and oper[0].isdigit():
        s = int(oper[0])
    elif v=='+':
        s+=int(oper[i+1])
    elif v=='-':
        s-=int(oper[i+1])
print(s)
