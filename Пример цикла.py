s1, s2 = input().split()
op = ['in','==', '!=', '<']
for i in op:
    print(eval(f's1 {i} s2'), end=' ')

