def check_password(password):
    def wrapper(func):
        def podwrapper(*args, **kwargs):
            ipassword = input('Введите пароль: ')
            if ipassword != password:
                print('В доступе отказано')
                return
            result = func(*args, **kwargs)
            return result
        return podwrapper
    return wrapper

@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print('Булочка')
    if withOnion:
        print('Луковые колечки')
    if withTomato:
        print('Ломтик помидора')
    print('Котлета из', typeOfMeat)
    print('Булочка')
