t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def text(a, sep='-'):
    b = ''
    for i in a:
        if i in t:
            b += t.get(i)
        elif i == ' ':
            b += sep
        else:
            b += i

    return b


r = input().lower()
print(text(r))
print(text(r, sep='+'))


# ----------------------------------------------

def trans(s: str, sep='-'):
    return s.replace(' ', sep).translate(s.maketrans(t))


s1 = input().lower()
print(trans(s1))
print(trans(s1, sep='+'))

# ------------------------------------------------


siper = str.maketrans(t)


def translate_cyrillic_latin(s, sep='-'):
    return sep.join(w.translate(siper) for w in s.lower().split())


s = input()
print(translate_cyrillic_latin(s))
print(translate_cyrillic_latin(s, '+'))
