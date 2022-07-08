"""import re

def email_parse(email):
        re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
        if not re_email.match(email):
            raise ValueError(f'wrong email: {email}')
        print(re_email.match(email).groupdict())

for i in ['someone@geekbrains.ru', 'someone@geekbrain.sru', 'someone33@geekbrai.nsru']:
    try:
        email_parse(i)
    except ValueError:
        print(ValueError)
"""
from functools import wraps

def loger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num_list = [el for el in (*args, *kwargs.values())]
        n = [f'{func.__name__}({len}: {type(el)})' for el in num_list]
        print(*n, *func(*args, **kwargs), sep=', \n')
    return wrapper

@loger
def cube(*x, **y):
    num_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i**3 for i in num_list]

a= cube(3, 13.5, 9, a=56.7, b=43)

def checker(l_func):
    def _checker(func):

        @wraps(func)

        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f'wrong val {num}')
        return wrapper
    return _checker

@checker(lambda x: x >0)
def cube(x):
    return x**3
try:
    a=cube(5)
    print(help(cube))
except (ValueError, TypeError) as err:
    print(err)
