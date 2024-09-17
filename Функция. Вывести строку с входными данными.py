def print_str():
    x, c = input().split()
    print(f"Уважаемый, {x} {c}! Вы верно выполнили это задание!")
    print("Уважаемый, " + x + ' ' + c + "! Вы верно выполнили это задание!")
    print("Уважаемый, %s %s! Вы верно выполнили  это задание!" % (x, c))


print_str()


# ----------------
def weigh_obj(x):
    print(f'Min = {min(x)}, max = {max(x)}, sum = {sum(x)}')


weigh_obj(list(map(int, input().split())))

#----------
def per_rectangle(width, height):
    print(f'Периметр прямоугольника, равен {2 * (width + height)}')

width, height = map(int, input().split())
per_rectangle(width, height)
