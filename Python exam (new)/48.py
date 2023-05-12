import inspect


def some_func(n, m, /, arg=None, dsa=None, *, qwe, **dq):
    pass


def func(subfunc=None):
    print(f'Анализируем функцию {subfunc.__name__}')
    for param in inspect.signature(subfunc).parameters.values():
        print(param.name, param.kind, sep=': ')


func(some_func)
