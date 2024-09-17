

def show_menu(func):
    def wrapper(*args, **kwargs):
        menu = func(*args)
        for i, j in enumerate(menu):
            print(f"{i+1}. {j}")

    return wrapper


@show_menu
def get_menu(s: str):
    return s.split()




print(get_menu('Главная Добавить Удалить Выйти'))
