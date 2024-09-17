t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def dev(func):
    def wrapper(*args, **kwargs):
        s = func(*args)
        while "--" in s:
            s = s.replace('--', '-')
        return s

    return wrapper

@dev
def str(str):
    s = ''
    for i in str:
        if i in t:
            s += t.get(i)
        elif i in [":", ";", ".", ",", "_", " "]:
            s += '-'
        else:
            s += i
    return s

s = str(input().lower())
print(s)