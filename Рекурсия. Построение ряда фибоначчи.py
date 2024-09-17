
def fib_rec(N, f=[1, 1]):
    if N > 2:
        f.append(f[-1] + f[-2])
        fib_rec(N - 1, f)
    return f

print(fib_rec(7))

#------------------------------------------------------------------------------
def fib_rec(N, f=[1, 1]):
    return fib_rec(N, f + [f[-2] + f[-1]]) if len(f) < N else f[:N]

#рез f[:N] нужен лишь для случая N=1, чтобы на выводе не оказались два числа 1 1.
