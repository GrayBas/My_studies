def fact_rec(n: int):
    if n <= 0:
        return 1
    else:
        return n * fact_rec(n-1)


print(fact_rec(6))

#------------------

def fact_rec(n):
    return n and n * fact_rec(n - 1) or 1