# Реализовать функцию repl, которая принимает на вход строку и набор заранее неизвестных параметров.
# Результатом функции является строка, в которой слова совпадающие с именами параметров заменены на значения параметров.
# Пример: строка: 'replace my val abc', параметры my='s1', abc='fff' -> Результат: 'replace s1 val fff'

def repl(string, **p):
    for k, v in p.items():
        if k in string:
            string = string.replace(k, v)
    return string


print(repl(string='replace my val abc', my='s1', abc='fff'))
