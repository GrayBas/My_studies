
def sort(func):
    def wrapper(*args, **kwargs):
        return sorted(func(*args))
    return wrapper




@sort
def get_list(s: str):
    return list(map(int, s.split()))

lst = get_list(input())
print(*lst)



