def check_password(func):
    password = '228'
    access_granted = False
    def wrapper(*args, **kwargs):
        nonlocal access_granted
        if not access_granted:
            ipassword = input('Введите пароль: ')
            if ipassword != password:
                print('В доступе отказано')
                return
            access_granted = True
        result = func(*args, **kwargs)
        return result
    return wrapper

@check_password
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
