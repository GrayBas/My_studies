def generate_numbers(N:int, M:int, prefix=None):
    """ Генерация всех чисел N-ричной системы счисление длиной M"""
    if M == 0:              
        print(*prefix)
        return
    prefix = prefix or []  # если None то ложь, поэтому or вернёт вторую ложь
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
        
generate_numbers(2, 2)


def generate_permutation(N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях,
        с префиксом prefix
    """
    M = N if M == -1 else M # По умолчанию N чисел в M позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutation(N, M-1, prefix)
        prefix.pop()

generate_permutation(3)        
        
    