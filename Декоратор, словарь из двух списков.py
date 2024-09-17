def dict(func):
    def wrapper(*args, **kwargs):
        s, h = func(*args)
        d = {s[i]: h[i] for i in range(len(s))}
        return d

    return wrapper


@dict
def str(*args):
    s = args[0].split()
    d = args[1].split()
    return s, d


d = str(input(), input())

print(*sorted(d.items()))
