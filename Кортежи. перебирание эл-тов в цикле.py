t = tuple(input().lower().split())

print(*(x for x in t if 'ва' in x))
print(*(t[x] for x in range(len(t)) if 'ва' in t[x]))
