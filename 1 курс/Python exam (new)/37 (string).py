import string


# string.ascii_letters - строка со всеми буквами английского алфавита
# (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
def nam_par(*p, name=string.ascii_letters):
    dic = {letter: par for letter, par in zip(name, p)}
    return dic


print(nam_par(7, 3, 1, 8, 10, 13, name='xyzafg'))
print(nam_par(21, 'val', -3.5))
